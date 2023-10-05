import requests
from bs4 import BeautifulSoup

def scrape_bass_guitar_info(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to fetch the webpage")
        return None
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Scrape relevant information from the webpage
    # Example: Get bass guitar names and features
    bass_guitar_names = [element.text for element in soup.find_all('h3', class_='bass-guitar-name')]
    bass_guitar_features = [element.text for element in soup.find_all('div', class_='bass-guitar-features')]
    
    return bass_guitar_names, bass_guitar_features

# Example usage
url = "https://example.com/bass_guitars"
bass_guitar_names, bass_guitar_features = scrape_bass_guitar_info(url)
print("Bass Guitar Names:", bass_guitar_names)
print("Bass Guitar Features:", bass_guitar_features)
