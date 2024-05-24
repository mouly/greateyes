"""Base scraper class for all county scrapers to inherit from."""
from abc import ABC, abstractmethod
import requests

class CountyScraper(ABC):
    """Base scraper class for all county scrapers to inherit from."""
    def __init__(self, url):
        self.url = url

    def check_for_new_meetings(self):
        """Check if there are new meetings available on the county website since date."""
        html_content = self.fetch_page()
        return self.parse_page(html_content)

    def fetch_page(self):
        """Fetch the HTML content of the county website."""
        response = requests.get(self.url, timeout=10)
        response.raise_for_status()
        return response.text

    @abstractmethod
    def parse_page(self, html_content):
        """Parse the HTML content of the county website."""
      