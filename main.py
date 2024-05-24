import pandas as pd
from playwright.sync_api import sync_playwright

def take_snapshot(url, snapshot_path):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        page.screenshot(path=snapshot_path)
        browser.close()

def main():
    # Read the CSV file
    df = pd.read_csv('websites.csv')

    # Iterate over the websites
    for i, row in df.iterrows():
        url = row['county']
        snapshot_path = f'snapshot_{i}.png'
        take_snapshot(url, snapshot_path)

if __name__ == '__main__':
    main()