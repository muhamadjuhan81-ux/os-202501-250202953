# 1. Gunakan image dasar Python yang ringan
FROM python:3.11-slim

# 2. Tentukan direktori kerja di dalam container
WORKDIR /app

# 3. Salin file kode kamu ke dalam container
COPY pemutaran_musik.py .

# 4. Perintah untuk menjalankan aplikasi saat container dimulai
CMD ["python", "-u", "pemutaran_musik.py"]
