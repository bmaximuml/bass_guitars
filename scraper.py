import argparse
from typing import List, Tuple
import os
import requests
from bs4 import BeautifulSoup

def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Bass Guitar Scraper")
    parser.add_argument("urls", nargs="*", default=os.getenv("SCRAPE_URLS", "").split(";"),
                        help="URLs to scrape, separated by space")
    parser.add_argument("--selector", "-s", default=os.getenv("SELECTOR", "h3.bass-guitar-name"),
                        help="CSS selector to use for scraping")
    args = parser.parse_args()
    return args

def scrape_bass_guitar_info(urls: List[str], selector: str) -> Tuple[List[str], List[str]]:
    bass_guitar_names = []
    bass_guitar_features = []

    for url in urls:
        response = requests.get(url)
        if response.status_code != 200:
            print("Failed to fetch the webpage")
            continue

        soup = BeautifulSoup(response.content, 'html.parser')

        # Scrape relevant information from the webpage
        # Example: Get bass guitar names and features
        bass_guitar_names.extend([element.text for element in soup.select(selector)])
        bass_guitar_features.extend([element.text for element in soup.select('div.bass-guitar-features')])

    return bass_guitar_names, bass_guitar_features

if __name__ == "__main__":
    args = parse_arguments()
    scraped_names, scraped_features = scrape_bass_guitar_info(args.urls, args.selector)
    print("Bass Guitar Names:", scraped_names)
    print("Bass Guitar Features:", scraped_features)
