from scrapers.counties import county_a_scraper, county_b_scraper

class ScraperFactory:
    @staticmethod
    def create_scraper(county_name, url):
        if county_name == "CountyA":
            return county_a_scraper.CountyAScraper(url)
        elif county_name == "CountyB":
            return county_b_scraper.CountyBScraper(url)
        # Add more counties as needed
        else:
            raise ValueError(f"Unknown county: {county_name}")
