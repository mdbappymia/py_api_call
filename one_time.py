import requests
import json
import sys
import os


def fetch_and_save(api_url, output_file, encoding="utf-8"):
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()

        with open(output_file, 'w', encoding=encoding) as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

        print(f"Data successfully saved to {output_file}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
    except json.JSONDecodeError:
        print("Error decoding JSON response")


# Replace with the actual API URL
api_url = "https://quranapi.pages.dev/api/9/15.json"
output_dir = os.path.join('ayath', '9')
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
output_file = output_dir+"/15.json"
encoding = "utf-8" if len(sys.argv) < 2 else sys.argv[1]
fetch_and_save(api_url, output_file, encoding)
