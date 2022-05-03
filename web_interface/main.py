import streamlit as st
from requests.exceptions import HTTPError

from integration import double_frame_rate


if __name__ == "__main__":
    st.set_page_config(page_title="FRI(Y)", page_icon="./static/icons/fry.png")

    app = st.container()
    app.title("Frame Rate Increaser")

    algorithm = st.sidebar.selectbox(
        "Interpolation algorithm", options=["linear", "radon"]
    )

    input_ct = app.container()
    uploaded_video = input_ct.file_uploader(
        "Choose a video file to double frame rate", type=["mp4"]
    )
    if uploaded_video is not None:
        input_ct.video(uploaded_video.getvalue())

        if app.button("Double frame rate (it might take some time)"):
            try:
                doubled_video_name, doubled_video_bytes = double_frame_rate(
                    uploaded_video.name, uploaded_video.getvalue(), algorithm
                )
                st.success("Frame rate doubled :sunglasses:")
            except HTTPError:
                st.error("Something went wrong :disappointed:")

            output = app.container()
            output.download_button(
                label="Download video with doubled frame rate",
                data=doubled_video_bytes,
                file_name=doubled_video_name,
                mime="video/mp4",
            )
