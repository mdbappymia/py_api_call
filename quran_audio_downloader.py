import requests
import os
from typing import Optional, Dict
import logging
from datetime import datetime

now = datetime.now()
current_date = now.strftime("%Y%m%d")

logging.basicConfig(
    filename=rf"log_{current_date}.log",
    format="%(asctime)s %(message)s",
    filemode="a",
)

def write_log(log):
    logging.warning(log)

def get_surah_info(surah_num: int) -> Optional[Dict]:
    try:
        url = f"https://quranapi.pages.dev/api/{surah_num}/1.json"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        return None
    except Exception as e:
        write_log(f"Error fetching surah info: {str(e)}")
        return None

def download_surah_audio(surah_num: int) -> None:
    surah_info = get_surah_info(surah_num)
    if not surah_info:
        write_log(f"Failed to get information for Surah {surah_num}")
        return

    total_ayat = surah_info.get('totalAyah', 0)
    if total_ayat == 0:
        write_log(f"Invalid total ayahs for Surah {surah_num}")
        return

    surah_dir = "audio/"+str(surah_num)
    if not os.path.exists(surah_dir):
        os.makedirs(surah_dir)

    for ayah_num in range(1, total_ayat + 1):
        url = f"https://everyayah.com/data/Abdurrahmaan_As-Sudais_192kbps/{str(surah_num).zfill(3)}{str(ayah_num).zfill(3)}.mp3"
        output_file = os.path.join(surah_dir, f"ayah_{ayah_num}.mp3")

        try:
            response = requests.get(url)
            if response.status_code == 200:
                with open(output_file, 'wb') as f:
                    f.write(response.content)
                write_log(f"Downloaded: Surah {surah_num}, Ayah {ayah_num}")
                print(f"Downloaded: Surah {surah_num}, Ayah {ayah_num}")
            else:
                write_log(
                    f"Failed to download: Surah {surah_num}, Ayah {ayah_num}")
        except Exception as e:
            write_log(
                f"Error downloading Surah {surah_num}, Ayah {ayah_num}: {str(e)}")


def main():
    for i in range(114):
        surah_num = str(i+1)
        download_surah_audio(surah_num)

if __name__ == "__main__":
    main()
