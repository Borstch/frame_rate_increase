import time
import json
from pathlib import Path
from argparse import ArgumentParser
from typing import Dict, Union, Optional

import numpy as np
from tqdm import tqdm

from metrics import msjd
from video import VideoReader
from processors import get_algorithm
from dtypes import FrameGenerator, IncreaseAlgorithm


class TestEngine:
	def __init__(self, path_to_test_videos: Path, algorithm: IncreaseAlgorithm):
		self.video_files = [video for video in path_to_test_videos.glob("*.mp4")]
		self.algorithm = algorithm

	def run_tests(self) -> None:
		tests_data = {video_file.stem: [] for video_file in self.video_files}
		for video_file in tqdm(self.video_files):
			for times in tqdm([2, 4, 8]):
				test_data = self.__run_video_test(video_file, times)
				tests_data[video_file.stem].append(test_data)

		with open(self.algorithm.value + "_test.json", "w") as f:
			json.dump(tests_data, f)

	def __run_video_test(self, video_file: Path, times: int) -> Dict[str, Union[int, float]]:
		interpolate = get_algorithm(self.algorithm)

		inputs_reader = VideoReader(video_file)
		gt_reader = VideoReader(video_file)

		original_fps = inputs_reader.fps

		X = self.__get_every_nth_frame(inputs_reader, times)
		Y = self.__get_every_not_nth_frame(gt_reader, times)

		x_prev = next(X)
		y_hats = []
		benchmarks = []
		for x in tqdm(X):
			ts = time.time()
			y_hat = interpolate(x_prev, x)
			te = time.time()

			y_hats.append(y_hat)
			benchmarks.append(te - ts)

		mean_distance = msjd(y_hats, Y)
		mean_benchmark = np.mean(benchmarks)

		return {"original_fps": original_fps, "modified_fps": original_fps * times, "msjd": mean_distance, "mean_time": mean_benchmark}


	@staticmethod
	def __get_every_nth_frame(reader: VideoReader, n: Optional[int] = 2) -> FrameGenerator:
		for i, frame in enumerate(reader):
			if i % n != 0:
				continue
			yield frame

	@staticmethod
	def __get_every_not_nth_frame(reader: VideoReader, n: Optional[int] = 2) -> FrameGenerator:
		for i, frame in enumerate(reader):
			if i % n == 0:
				continue
			yield frame


if __name__ == '__main__':
	parser = ArgumentParser()
	parser.add_argument("test_folder", type=Path, help="Path to the folder with test videos")
	parser.add_argument("algorithm", type=IncreaseAlgorithm, help="Algorithm to use in test")

	args = parser.parse_args()

	engine = TestEngine(args.test_folder, args.algorithm)
	engine.run_tests()
