import argparse
import os
from bs4 import BeautifulSoup
import requests

def parse_arguments():
    parser = argparse.ArgumentParser(description="Bass Guitar Scraper")
    parser.add_argument("urls", nargs="*", default=os.getenv("SCRAPE_URLS", "").split(";"),
                        help="URLs to scrape, separated by space")
    parser.add_argument("--selector", "-s", default=os.getenv("SELECTOR", "h3.bass-guitar-name"),
                        help="CSS selector to use for scraping")
    args = parser.parse_args()
    return args

def scrape_bass_guitar_info(urls, selector):
    for url in urls:
        response = requests.get(url)
        if response.status_code != 200:
            print("Failed to fetch the webpage")
            continue
        
        soup = BeautifulSoup(response.content, 'html.parser')
        elements = soup.select(selector)
        # Extract information based on the provided selector
        for element in elements:
            print(element.text)

if __name__ == "__main__":
    args = parse_arguments()
    scrape_bass_guitar_info(args.urls, args.selector)
