import requests
import os
from typing import Optional
import logging
from datetime import datetime
import os

# For write log
now = datetime.now()
current_date = now.strftime("%Y%m%d")
log_dir = "logs\\"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)
logging.basicConfig(
    filename=log_dir + rf"log_{current_date}.log",
    format="%(asctime)s %(message)s",
    filemode="a",
)


def write_log(log):
    logging.warning(log)


def download_surah_audio(surah_num: int, ayah_num: int) -> None:
    """
    Download audio files for all ayahs of a specific surah

    Args:
        surah_num (int): Surah number (1-114)
        total_ayat (int): Total number of ayahs in the surah
    """
    # Create directory for surah if it doesn't exist
    surah_dir = str(surah_num)
    if not os.path.exists(surah_dir):
        os.makedirs(surah_dir)

    # Download each ayah
    # for ayah_num in range(1, total_ayat + 1):
        url = f"https://quranaudio.pages.dev/3/{surah_num}_{ayah_num}.mp3"
        output_file = os.path.join(surah_dir, f"ayah_{ayah_num}.mp3")

        try:
            response = requests.get(url)
            if response.status_code == 200:
                with open(output_file, 'wb') as f:
                    f.write(response.content)
                print(f"Downloaded: Surah {surah_num}, Ayah {ayah_num}")
            else:
                print(
                    f"Failed to download: Surah {surah_num}, Ayah {ayah_num}")
        except Exception as e:
            print(
                f"Error downloading Surah {surah_num}, Ayah {ayah_num}: {str(e)}")


def main():
    # Example usage
    surah_num = int(input("Enter surah number (1-114): "))
    total_ayat = int(input("Enter total number of ayahs in the surah: "))

    if 1 <= surah_num <= 114:
        download_surah_audio(surah_num, total_ayat)
    else:
        print("Invalid surah number. Please enter a number between 1 and 114.")


if __name__ == "__main__":
    main()
