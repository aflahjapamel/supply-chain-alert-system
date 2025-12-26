import requests
import os
import logging
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
load_dotenv()

class FlightDataIngestor:
    def __init__(self):
        self.client_id = os.getenv("OPENSKY_CLIENT_ID")
        self.client_secret = os.getenv("OPENSKY_CLIENT_SECRET")
        self.token_url = "https://auth.opensky-network.org/auth/realms/opensky-network/protocol/openid-connect/token"
        self.api_url = "https://opensky-network.org/api/states/all"
        self.access_token = None

    def get_access_token(self):
        """Menukar Client ID & Secret dengan Access Token (Standard OAuth2)"""
        data = {
            'grant_type': 'client_credentials',
            'client_id': self.client_id,
            'client_secret': self.client_secret,
        }
        try:
            response = requests.post(self.token_url, data=data)
            response.raise_for_status()
            self.access_token = response.json().get('access_token')
            logging.info("Access Token berhasil didapatkan.")
        except Exception as e:
            logging.error(f"Gagal mendapatkan token: {e}")

    def fetch_live_flights(self):
        """Menarik data seluruh pesawat di wilayah udara Indonesia"""
        if not self.access_token:
            self.get_access_token()

        headers = {"Authorization": f"Bearer {self.access_token}"}
        
        # Bounding Box Seluruh Indonesia
        params = {
            'lamin': -11.0, 
            'lomin': 95.0, 
            'lamax': 6.0, 
            'lomax': 141.0
        }
        
        try:
            logging.info("Memantau seluruh wilayah udara Indonesia...")
            response = requests.get(self.api_url, headers=headers, params=params, timeout=15)
            response.raise_for_status()
            
            data = response.json()
            states = data.get('states')
            
            if states is not None:
                logging.info(f"Berhasil! Terdeteksi {len(states)} pesawat di Indonesia.")
                return states
            else:
                logging.info("Koneksi berhasil, namun saat ini tidak ada pesawat terdeteksi di Indonesia.")
                return []
                
        except Exception as e:
            logging.error(f"Error saat fetch data Indonesia: {e}")
            return None

if __name__ == "__main__":
    ingestor = FlightDataIngestor()
    flights = ingestor.fetch_live_flights()