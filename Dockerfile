FROM python:3.10-slim

# 1) Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg gcc libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# 2) Set working directory
WORKDIR /app

# 3) Copy requirements first (agar cache pip bisa dipakai)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4) Copy all project files
COPY . .

# 5) Expose port Streamlit
EXPOSE 8501

# 6) Default command
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
