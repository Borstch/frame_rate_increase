import base64
from typing import Tuple

import requests
from requests.exceptions import HTTPError


def encode_video(video: bytes) -> str:
	return base64.b64encode(video).decode()


def decode_video(video_string: str) -> bytes:
	return base64.decodebytes(bytes(video_string, "utf-8"))


def double_frame_rate(filename: str, content: bytes, algorithm: str) -> Tuple[str, bytes]:
	payload = {"filename": filename, "content": encode_video(content)}
	response = requests.post("http://increaser:80/video/double_fps", params={"algorithm": algorithm}, json=payload)

	if response.status_code != 200:
		raise HTTPError(f"Can't process file {filename}. Something went wrong: {response.status_code}")

	response_json = response.json()
	return response_json["filename"], decode_video(response_json["content"])
