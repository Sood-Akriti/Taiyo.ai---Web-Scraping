# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 11:51:01 2023

@author: A
"""

import unittest
import logging
from scraper import EprocureScraper

class TestEprocureScraper(unittest.TestCase):
    def test_scrape(self):
        scraper = EprocureScraper()
        scraper.scrape()
        self.assertTrue(os.path.exists(scraper.output_file))

if __name__ == '__main__':
    logging.basicConfig(filename="client.log", level=logging.INFO)
    logging.info("Starting client")
    unittest.main()
    logging.info("Client finished")