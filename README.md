# ✈️ Supply Chain Early Warning System: Indonesia Air Cargo Risk Monitor

## 🎯 Business Impact

Sistem ini memantau seluruh wilayah udara Indonesia secara real-time untuk mendeteksi risiko keterlambatan pengiriman kargo udara. Dengan mengintegrasikan data posisi pesawat dan kondisi cuaca lokal, sistem ini memberikan peringatan dini kepada manajer logistik untuk:

- **Mengoptimalkan Armada:** Mengalihkan truk penjemputan jika pesawat tujuan terdeteksi masuk ke zona cuaca buruk.
- **Efisiensi Biaya:** Mengurangi biaya operasional idle sebesar estimasi **12%** melalui manajemen waktu penjemputan yang lebih akurat.

## 🏗️ Production-Ready Architecture

Proyek ini dibangun dengan arsitektur modular untuk memastikan skalabilitas dan kemudahan pemeliharaan:

- `data_ingestion.py`: Menangani komunikasi dengan **OpenSky Network API** menggunakan protokol **OAuth2**.
- `weather_engine.py`: Mengambil data cuaca real-time dari **OpenWeather API** berdasarkan koordinat GPS pesawat.
- `main.py`: _Orchestrator_ yang menggabungkan kedua sumber data dan menjalankan logika analisis risiko bisnis.

## 🛠️ Key Technical Challenges Overcome

Dalam pengembangan ini, saya berhasil mengatasi beberapa tantangan teknis tingkat lanjut:

1. **Modern Authentication (OAuth2):** Mengimplementasikan sistem penukaran _Client ID_ & _Secret_ menjadi _Bearer Token_ untuk mengikuti standar keamanan terbaru OpenSky.
2. **Data Validation & Integrity:** Memperbaiki anomali pemetaan data di mana indeks ketinggian (_altitude_) sempat terbaca sebagai koordinat, serta menangani nilai `None` pada respon API untuk mencegah _system crash_.
3. **Geofencing & Scalability:** Memperluas cakupan pemantauan dari skala lokal (Jakarta) menjadi skala nasional (seluruh Indonesia).

## 🚀 Setup & Installation

1. Clone repository ini.
2. Buat environment menggunakan **Conda**:
   ```bash
   conda create -n supply-chain-env python=3.10
   conda activate supply-chain-env
   pip install -r requirements.txt
   ```
