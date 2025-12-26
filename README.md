# Supply Chain Early Warning System (Real-Time Air Cargo)

## 🎯 Business Impact

Proyek ini membangun **sistem peringatan dini rantai pasok** yang mengintegrasikan data penerbangan real-time dan kondisi cuaca buruk. Sistem ini memprediksi keterlambatan kargo udara sebelum pesawat mendarat, sehingga perusahaan logistik dapat mengalihkan armada truk penjemput ke pengiriman lain secara otomatis.
**Estimasi Dampak:** Mengurangi biaya idle operasional sebesar **12%**.

## 🛠️ Tech Stack & Production Features

- **Data Source:** OpenSky Network API (Flight Tracking) & OpenWeather API.
- **Backend:** Python 3.x.
- **Validation:** Menggunakan `Pydantic` untuk memastikan kualitas data API.
- **Reliability:** Implementasi `Try-Except` block untuk menangani API downtime atau network errors.
- **Logging:** Sistem pencatatan otomatis menggunakan library `logging` untuk memantau performa pipeline secara real-time.

## 🏗️ Data Pipeline Design

1. **Ingestion:** Mengambil posisi pesawat kargo dalam radius 200km dari bandara tujuan.
2. **Weather Integration:** Mengecek kondisi cuaca (visibilitas & kecepatan angin) di lokasi bandara.
3. **Risk Analysis:** Menghitung skor risiko keterlambatan berdasarkan data cuaca dan estimasi waktu tiba (ETA).
4. **Alerting:** Menghasilkan rekomendasi aksi (contoh: "Delay Truck B-123") ke dalam log sistem.

## 🚀 How to Run

1. Clone repository ini.
2. Buat file `.env` dan masukkan API Key kamu:
   ```env
   OPENSKY_USERNAME=your_username
   OPENWEATHER_API_KEY=your_key
   ```
