import streamlit as st
import tempfile, os
from utils import process_video_pipeline

st.title("📤 Upload Video")

uploaded_file = st.file_uploader("Upload video", type=["mp4", "mov", "avi", "mkv"])

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as tmp_video:
        tmp_video.write(uploaded_file.read())
        video_path = tmp_video.name

    st.video(video_path)

    if st.button("🚀 Proses Video"):
        with st.spinner("Sedang memproses..."):
            transcript, summary = process_video_pipeline(video_path, mode="short")

        if transcript and summary:
            st.subheader("📝 Transkrip")
            st.text_area("Hasil Transkrip:", transcript, height=200)

            st.subheader("📌 Ringkasan")
            st.write(summary)

            st.download_button(
                "💾 Download Ringkasan",
                data=summary,
                file_name="summary.txt",
                mime="text/plain"
            )

    if os.path.exists(video_path):
        os.remove(video_path)
