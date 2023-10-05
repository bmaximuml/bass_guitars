import unittest
from unittest import mock
from scraper import scrape_bass_guitar_info

class TestBassGuitarScraper(unittest.TestCase):

    @mock.patch('scraper.requests.get')
    def test_scrape_bass_guitar_info(self, mock_get):
        # Mocking the response content
        mock_response = mock.Mock()
        mock_response.status_code = 200
        mock_response.content = """
            <html>
                <body>
                    <h3 class="bass-guitar-name">Bass Guitar 1</h3>
                    <h3 class="bass-guitar-name">Bass Guitar 2</h3>
                </body>
            </html>
        """
        mock_get.return_value = mock_response

        urls = ['https://example.com/bass_guitars']
        selector = 'h3.bass-guitar-name'
        bass_guitar_names, _ = scrape_bass_guitar_info(urls, selector)
        expected_names = ['Bass Guitar 1', 'Bass Guitar 2']

        self.assertEqual(bass_guitar_names, expected_names)

if __name__ == '__main__':
    unittest.main()
