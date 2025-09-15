import os
import yt_dlp
from openai import OpenAI
import whisper
import ffmpeg
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def download_youtube_video(url, output_path="downloads"):
    """
    Download video YouTube pakai yt-dlp.
    """
    try:
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        ydl_opts = {
            "format": "mp4/bestaudio/best",
            "outtmpl": os.path.join(output_path, "%(title)s.%(ext)s"),
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            file_path = ydl.prepare_filename(info)
            return file_path
    except Exception as e:
        print("Error:", e)
        return None

def process_video_pipeline(video_path: str, mode: str = "short"):
    """
    Full pipeline: video -> audio -> transkrip -> ringkasan
    """
    try:
        # 1. Ekstrak audio
        audio_path = extract_audio(video_path)

        # 2. Transkrip dengan Whisper
        transcript = transcribe_whisper(audio_path)

        # 3. Ringkas dengan GPT
        summary = summarize_gpt(transcript, mode=mode)

        return transcript, summary
    except Exception as e:
        print("Error pipeline:", e)
        return None, None

def extract_audio(video_path: str, output_path: str = None) -> str:
    """
    Extract audio from video using ffmpeg.
    """
    try:
        if output_path is None:
            output_path = video_path.replace('.mp4', '.wav').replace('.mov', '.wav').replace('.avi', '.wav')
        
        # Extract audio using ffmpeg
        (
            ffmpeg
            .input(video_path)
            .output(output_path, acodec='pcm_s16le', ac=1, ar='16k')
            .overwrite_output()
            .run(quiet=True)
        )
        return output_path
    except Exception as e:
        print(f"Error extracting audio: {e}")
        return None

def transcribe_whisper(audio_path: str) -> str:
    """
    Transcribe audio using OpenAI Whisper.
    """
    try:
        # Load Whisper model
        model = whisper.load_model("base")
        
        # Transcribe audio
        result = model.transcribe(audio_path)
        return result["text"]
    except Exception as e:
        print(f"Error transcribing: {e}")
        return None

def summarize_gpt(transcript: str, mode: str = "short") -> str:
    """
    Summarize transcript using OpenAI GPT.
    """
    try:
        # Get API key from environment
        api_key = os.getenv("OPENAI_API_KEY")
        
        if not api_key:
            return "Error: OpenAI API key not found. Please set OPENAI_API_KEY environment variable."
        
        client = OpenAI(api_key=api_key)

        if mode == "short":
            prompt = f"Buat ringkasan singkat dari transkrip berikut dalam bahasa Indonesia:\n\n{transcript}"
            max_tokens = 500
        else:
            prompt = f"Buat ringkasan detail dari transkrip berikut dalam bahasa Indonesia:\n\n{transcript}"
            max_tokens = 1000

        response = client.chat.completions.create(
            model="gpt-4o-mini",  # atau "gpt-4o"
            messages=[
                {"role": "system", "content": "Anda adalah asisten yang ahli dalam membuat ringkasan yang jelas dan informatif."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=max_tokens,
            temperature=0.7
        )

        return response.choices[0].message.content

    except Exception as e:
        print(f"Error summarizing: {e}")
        return f"Error: {str(e)}"
