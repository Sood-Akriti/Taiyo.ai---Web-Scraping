import requests
from bs4 import BeautifulSoup
import pandas as pd
import logging
import os
from config import Config

class EprocureScraper:
    def __init__(self, url=Config.URL, output_file=Config.OUTPUT_FILE):
        self.url = url
        self.output_file = output_file

    def scrape(self):
        logging.basicConfig(filename="scraper.log", level=logging.INFO)
        logging.info("Scraping started")
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, 'html.parser')
        results = soup.find(id='results')
        tender_elems = results.find_all('tr')

        tenders = []
        for tender_elem in tender_elems:
            tender = {}
            columns = tender_elem.find_all('td')
            if columns:
                tender['Tender Number'] = columns[0].text.strip()
                tender['Department'] = columns[1].text.strip()
                tender['Product Category'] = columns[2].text.strip()
                tender['Last Date'] = columns[3].text.strip()
                tenders.append(tender)

        df = pd.DataFrame(tenders)
        df.to_csv(self.output_file, index=False)
        logging.info("Scraping finished")







