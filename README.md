# Video Summarizer App

Aplikasi Streamlit untuk men-transkrip dan meringkas video (file lokal maupun YouTube) menggunakan Whisper dan GPT.

## Fitur

- Upload video lokal (`pages/Upload_Videos.py`)
- Download dan proses video YouTube (`pages/Link_Video.py`)
- Transkripsi audio menggunakan Whisper (local)
- Ringkasan menggunakan OpenAI GPT
- Download ringkasan sebagai file `.txt`

## Prasyarat

- Python 3.10+ (disarankan)
- FFmpeg terpasang di sistem
- OpenAI API Key aktif
- (Opsional) GPU + CUDA untuk percepatan Whisper

## Instalasi

1. Clone repo dan masuk ke folder proyek:

```bash
git clone <repo-url>
cd video-summarizer
```

2. Buat dan aktifkan virtual environment (opsional tapi disarankan):

```bash
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
# macOS/Linux
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

4. Install FFmpeg

- Windows: download dari `https://ffmpeg.org/download.html` lalu tambahkan `bin/` ke PATH
- macOS: `brew install ffmpeg`
- Linux (Debian/Ubuntu): `sudo apt-get update && sudo apt-get install -y ffmpeg`

5. Konfigurasi environment variables

Buat file `.env` di root proyek berisi:

```env
OPENAI_API_KEY=your_api_key_here
```

Variabel opsional lain (sesuaikan jika tersedia di `utils.py`):

- `WHISPER_MODEL` (default: `base`)
- `SUMMARY_MODE` (`short`/`long`)

## Menjalankan Aplikasi (Local)

```bash
streamlit run app.py
```

Kemudian buka link yang ditampilkan (biasanya `http://localhost:8501`).

## Penggunaan

- Halaman Upload Video

  - Buka tab Upload Video
  - Pilih file video lokal (mp4, mkv, mov, dll.)
  - Klik proses untuk melakukan transkrip dan ringkasan
  - Setelah selesai, Anda bisa melihat transkrip, ringkasan, dan mengunduh ringkasan `.txt`

- Halaman Link Video YouTube
  - Buka tab Link Video YouTube
  - Tempel URL video YouTube
  - Klik "Proses Video YouTube"
  - Aplikasi akan mengunduh video, melakukan transkrip, dan menghasilkan ringkasan
  - Gunakan tombol "Download Ringkasan" untuk menyimpan ringkasan sebagai `.txt`

## Struktur Proyek

- `app.py` — entrypoint Streamlit, mengatur navigasi pages
- `utils.py` — utilitas untuk unduh YouTube, ekstraksi audio, transkrip, ringkasan
- `pages/`
  - `Upload_Videos.py` — proses video lokal
  - `Link_Video.py` — proses video dari URL YouTube
- `downloads/` — folder cache unduhan video/audio
- `sample_videos/` — contoh video (opsional)

## Docker (Opsional)

Jalankan dengan Docker dan docker-compose:

```bash
docker compose up --build
```

Pastikan Anda meneruskan `OPENAI_API_KEY` ke container (lihat `docker-compose.yml`).

## Tips Performa

- Gunakan model Whisper yang lebih kecil (`base`, `small`) untuk proses cepat; gunakan `medium`/`large` untuk akurasi lebih baik.
- Jika memiliki GPU, instal PyTorch dengan CUDA sesuai versi driver Anda agar transkripsi jauh lebih cepat.

## Troubleshooting

- FFmpeg tidak ditemukan

  - Pastikan FFmpeg sudah terinstal dan path `ffmpeg` bisa dipanggil dari terminal (cek: `ffmpeg -version`).

- Error autentikasi OpenAI

  - Pastikan `OPENAI_API_KEY` benar dan sudah dimuat di environment (restart terminal atau IDE jika perlu).

- Unduhan YouTube gagal

  - Beberapa video dilindungi atau rate-limited. Coba ulang, atau gunakan koneksi berbeda.

- Memori habis saat transkripsi
  - Gunakan model Whisper lebih kecil, atau proses video yang lebih pendek.

## Keamanan & Biaya

- Ringkasan menggunakan API OpenAI dan akan menimbulkan biaya sesuai penggunaan token.
- Hindari mengunggah konten yang sensitif atau dilindungi hak cipta tanpa izin.

## Lisensi

Dirilis di bawah lisensi MIT. Lihat file `LICENSE`.
