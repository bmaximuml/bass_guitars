import unittest
from scraper import scrape_bass_guitar_info

class TestBassGuitarScraper(unittest.TestCase):

    def test_scrape_bass_guitar_info(self):
        urls = ['https://example.com/bass_guitars']
        selector = 'h3.bass-guitar-name'
        bass_guitar_names, _ = scrape_bass_guitar_info(urls, selector)
        self.assertEqual(bass_guitar_names, ['Bass Guitar 1', 'Bass Guitar 2'])

if __name__ == '__main__':
    unittest.main()
