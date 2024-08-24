from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import time
from src.laptop_ml.utils import DataGatheringConfig



class DataGathering:
    def __init__(self,config: DataGatheringConfig):
        self.config=config
        self.driver=webdriver.Chrome()

    def load_page(self):
        self.driver.get(self.config.source_url)
        time.sleep(3)
        old_height = self.driver.execute_script('return document.body.scrollHeight')
        while True:

            self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/div[1]/div[3]/div[3]').click()
            time.sleep(2)

            new_height = self.driver.execute_script('return document.body.scrollHeight')

            if new_height == old_height:
                break

            old_height = new_height

    def extract_html(self):
        html = self.driver.page_source

        with open(self.config.local_data_file,'w',encoding='utf-8') as f:
            f.write(html)

    def close_driver(self):
        self.driver.quit()
