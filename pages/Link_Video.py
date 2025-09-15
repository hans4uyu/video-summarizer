import streamlit as st
import tempfile, os
from utils import download_youtube_video, process_video_pipeline

st.title("🔗 Link Video YouTube")

video_url = st.text_input("Masukkan URL YouTube:", placeholder="https://www.youtube.com/watch?v=...")

if video_url and st.button("🚀 Proses Video YouTube"):
    with st.spinner("Mengunduh video..."):
        video_path = download_youtube_video(video_url)

    if video_path:
        st.video(video_path)

        with st.spinner("Sedang memproses..."):
            transcript, summary = process_video_pipeline(video_path, mode="short")

        if transcript and summary:
            st.subheader("📝 Transkrip")
            st.text_area("Hasil Transkrip:", transcript, height=200)

            st.subheader("📌 Ringkasan")
            st.write(summary)
            # Tombol untuk mengunduh ringkasan sebagai file teks
            file_name = f"{os.path.splitext(os.path.basename(video_path))[0]}_ringkasan.txt"
            st.download_button(
                label="⬇️ Download Ringkasan",
                data=str(summary),
                file_name=file_name,
                mime="text/plain",
            )
