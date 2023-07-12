from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

import stringsForScraper as st_scraper
import scraperAuxFunctions as saux
import searchFunctions
class WebsiteScraper:
    def __init__(self, driver_path):
        self.driver_path = driver_path
        self.driver = None
        self.wait = None
        self.refresh = 0
        self.search_function = None
    def start(self, URL, wait=15):
        service = Service(self.driver_path)
        self.driver = webdriver.Chrome(service=service)
        self.driver.get(URL)
        self.wait = WebDriverWait(self.driver, wait)

    def check_captcha(self, words_to_check):
        if any(word in self.driver.page_source for word in words_to_check):
            input('Please solve the CAPTCHA and press Enter to continue...')

    def set_search_function(self, search_function):
        self.search_function = search_function

    def search(self):
        self.search_function(self.driver)

    def close(self):
        if self.driver:
            self.driver.quit()


if __name__ == '__main__':

    words_to_check = st_scraper.words_to_check
    URL = st_scraper.URL
    PATH = st_scraper.PATH
    start = time.time()

    scraper = WebsiteScraper(PATH)
    scraper.start(URL)
    scraper.set_search_function(searchFunctions.search_moss)
    scraper.search()
    scraper.close()