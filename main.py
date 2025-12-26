import logging
from data_ingestion import FlightDataIngestor
from weather_engine import WeatherEngine

# Setup Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def analyze_supply_chain_risk():
    # 1. Inisialisasi Ingestor (Standard Production)
    flight_ingestor = FlightDataIngestor()
    weather_engine = WeatherEngine()

    # 2. Ambil Data Pesawat (Indonesia)
    logging.info("Memulai pemindaian risiko kargo udara Indonesia...")
    flights = flight_ingestor.fetch_live_flights()

    if not flights:
        logging.warning("Tidak ada data penerbangan untuk dianalisis.")
        return

    # 3. Analisis Risiko (Business Logic)
    for flight in flights[:5]:
        callsign = flight[1].strip() if flight[1] else "UNKNOWN"
        
        # PERBAIKAN INDEKS:
        # Indeks 5 adalah Longitude, Indeks 6 adalah Latitude
        lon = flight[5] 
        lat = flight[6]
        alt = flight[7] # Ini adalah angka 11000-an yang tadi terbaca sebagai longitude
        
        if lat and lon:
            # Sekarang kita mengirimkan koordinat yang benar ke OpenWeather
            weather = weather_engine.get_weather(lat, lon)
            
            if weather:
                condition = weather['condition']
                wind_speed = weather['wind_speed']
                
                is_risky = wind_speed > 10 or "rain" in condition or "thunderstorm" in condition
                status = "⚠️ RISIKO TINGGI" if is_risky else "✅ AMAN"
                
                logging.info(f"Pesawat: {callsign} | Alt: {alt}m | Lokasi: ({lat}, {lon})")
                logging.info(f"Cuaca: {condition}, Angin: {wind_speed} m/s | Status: {status}")
                
                if is_risky:
                    # Komponen 6: Communication (Actionable Insight)
                    print(f"\n--- ALERT UNTUK LOGISTIK ---")
                    print(f"Pesawat {callsign} terdeteksi dalam cuaca buruk.")
                    print(f"Rekomendasi: Siapkan rencana penjemputan alternatif di bandara tujuan.\n")
                print("-" * 30)

if __name__ == "__main__":
    analyze_supply_chain_risk()