import requests
import os

# Set up Riot API constants
API_KEY = 'RGAPI-ab240212-598f-47a9-a8bc-7e002cc90e35'  # Replace with your Riot API key
VERSION = '13.1.1'  # Replace with current version if necessary
BASE_URL = f'http://ddragon.leagueoflegends.com/cdn/{VERSION}/img'

# Directory to store assets
ASSETS_DIR = 'league_assets'

# Function to download image and save locally
def download_image(url, folder, filename):
    os.makedirs(folder, exist_ok=True)
    response = requests.get(url)
    if response.status_code == 200:
        with open(os.path.join(folder, filename), 'wb') as f:
            f.write(response.content)
        print(f"Downloaded {filename}")
    else:
        print(f"Failed to download {filename} from {url}")

# Get champion images
def fetch_champions():
    champs_url = f'http://ddragon.leagueoflegends.com/cdn/{VERSION}/data/en_US/champion.json'
    response = requests.get(champs_url)
    champions = response.json()['data']

    for champ_name, champ_data in champions.items():
        champ_id = champ_data['id']
        champ_image_url = f"{BASE_URL}/champion/{champ_id}.png"
        download_image(champ_image_url, f"{ASSETS_DIR}/champions", f"{champ_id}.png")

# Get minion images (as an example, using placeholders for custom assets)
def fetch_minions():
    minion_types = ['melee', 'caster', 'siege']
    for minion in minion_types:
        minion_url = f"{BASE_URL}/sprite/minion_{minion}.png"  # This URL structure may vary
        download_image(minion_url, f"{ASSETS_DIR}/minions", f"{minion}.png")

# Get map elements (bushes, etc.)
def fetch_map_elements():
    # Riot API doesn't provide direct links to elements like bushes, so here’s an example.
    # Assuming there's an image for each map element
    element_types = ['bush', 'tower', 'inhibitor']
    for element in element_types:
        element_url = f"{BASE_URL}/sprite/{element}.png"  # This URL is hypothetical
        download_image(element_url, f"{ASSETS_DIR}/map_elements", f"{element}.png")

# Fetch all assets
def fetch_all_assets():
    print("Fetching champions...")
    fetch_champions()

    print("Fetching minions...")
    fetch_minions()

    print("Fetching map elements...")
    fetch_map_elements()

# Execute fetching
if __name__ == "__main__":
    fetch_all_assets()
