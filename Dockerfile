FROM python:3.10-slim

# 1) Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg gcc \
    && rm -rf /var/lib/apt/lists/*

# 2) Set working directory
WORKDIR /app

# 3) Copy requirements & install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4) Copy source code
COPY . .

# 5) Expose Streamlit port
EXPOSE 8501

# 6) Run Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
