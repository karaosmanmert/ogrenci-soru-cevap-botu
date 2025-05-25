

import pandas as pd
import os

# CSV dosyasinin yolu
DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'sorular_cevaplar.csv')

def load_data(file_path: str = DATA_PATH) -> pd.DataFrame:
    try:
        if not os.path.exists(file_path):
            print(f"Hata: CSV dosyasi bulunamadi: {file_path}")
            return None
        
        df = pd.read_csv(file_path)
        
        # Gerekli sutunlarin varliğini kontrol edelim
        if "Soru" not in df.columns or "Cevap" not in df.columns:
            print("Hata: CSV dosyasinda 'Soru' ve 'Cevap' sutunlari bulunamadi.")
            return None
            
        print(f"'{file_path}' dosyasindan {len(df)} satir basariyla yuklendi.")
        return df
    except Exception as e:
        print(f"CSV yuklenirken hata olustu: {e}")
        return None
