import os
import requests
import time
from random import randint

# Define team names and corresponding logo URLs
team_logos = {
    "napoli": "https://upload.wikimedia.org/wikipedia/en/2/2d/SSC_Napoli_logo.svg",
    "atletico": "https://upload.wikimedia.org/wikipedia/en/f/f4/Atletico_Madrid_2017_logo.svg",
    "inter_milan": "https://upload.wikimedia.org/wikipedia/en/0/0b/FC_Internazionale_Milano_2021.svg",
    "juventus": "https://upload.wikimedia.org/wikipedia/en/6/6a/Juventus_FC_2017_logo.svg",
    "bayern": "https://upload.wikimedia.org/wikipedia/commons/1/1f/FC_Bayern_München_logo_%282017%29.svg"
}

# Create a directory to store team logos
os.makedirs('team_logos', exist_ok=True)

# Download and save team logos
for team, url in team_logos.items():
    file_extension = url.split('.')[-1]
    file_path = os.path.join('team_logos', f"{team}.{file_extension}")

    if os.path.exists(file_path):
        print(f"✅ {team} logo already exists, skipping download.")
        continue

    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

        print(f"📥 Downloading logo for {team}...")
        response = requests.get(url, headers=headers, timeout=15)

        # Add a random delay to reduce the risk of being blocked
        sleep_time = randint(4, 8)
        time.sleep(sleep_time)

        if response.status_code == 200:
            with open(file_path, 'wb') as file:
                file.write(response.content)
            print(f"✅ {team} logo successfully downloaded and saved to {file_path} (delay {sleep_time}s)")
        else:
            print(f"❌ Failed to download {team} logo. HTTP Status Code: {response.status_code}")

    except Exception as e:
        print(f"⚠️ Error occurred while downloading {team} logo: {e}")
