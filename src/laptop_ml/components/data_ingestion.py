import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from src.laptop_ml.entity import DataIngestionConfig



class DataIngestion:
    def __init__(self,config: DataIngestionConfig):
        self.driver=webdriver.Chrome()
        self.config=config
        self.name=[]
        self.price=[]
        self.ratings=[]
        self.num_rating_reviews=[]
        self.general=[]
        self.display=[]
        self.performance=[]
        self.connectivity=[]
        self.battery=[]
        self.others=[]
        self.html=None
        self.soup=None
        self.df=None
        

    def read_html(self):
        with open(self.config.html_file_path,'r',encoding='utf-8') as f:
            self.html = f.read()
        self.soup = BeautifulSoup(self.html,'lxml')

    def extractor(self):
        try:
            self.name.append(self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/div[1]/div[2]/div[1]/div[1]/h1').text)
        except:
            self.name.append(np.nan)
        try:
            self.price.append(self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/div[1]/div[2]/div[1]/div[1]/div/div[2]/strong').text)
        except:
            self.price.append(np.nan)
        try:
            self.ratings.append(self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/div[1]/div[2]/div[1]/div[1]/div/div[1]/span[2]').text)
        except:
            self.ratings.append(np.nan)
        try:
            self.num_rating_reviews.append(self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/div[1]/div[2]/div[1]/div[1]/div/div[1]/span[1]').get_attribute('style'))
        except:
            self.num_rating_reviews.append(np.nan)


        specs=self.soup.find("div",{"class":"sm-quick-specs"}).find_all("ul")
        list=[]
        if len(specs)==5:
            for j in specs[0].find_all("li"):
                list.append(j.text)
            self.general.append(list)
            list=[]
            for j in specs[1].find_all("li"):
                list.append(j.text)
            self.display.append(list)
            list=[]
            for j in specs[2].find_all("li"):
                list.append(j.text)
            self.performance.append(list)
            list=[]
            for j in specs[3].find_all("li"):
                list.append(j.text)
            self.connectivity.append(list)
            list=[]
            for j in specs[4].find_all("li"):
                list.append(j.text)
            self.battery.append(list)
            self.others.append(np.nan)
        elif len(specs)>5:
            for j in specs[0].find_all("li"):
                list.append(j.text)
            self.general.append(list)
            list=[]
            for j in specs[1].find_all("li"):
                list.append(j.text)
            self.display.append(list)
            list=[]
            for j in specs[2].find_all("li"):
                list.append(j.text)
            self.performance.append(list)
            list=[]
            for j in specs[3].find_all("li"):
                list.append(j.text)
            self.connectivity.append(list)
            list=[]
            for j in specs[4].find_all("li"):
                list.append(j.text)
            self.battery.append(list)
            list=[]
            for j in specs[5].find_all("li"):
                list.append(j.text)
            self.others.append(list)
            
        else:
            for j in specs[0].find_all("li"):
                list.append(j.text)
            self.general.append(list)
            list=[]
            for j in specs[1].find_all("li"):
                list.append(j.text)
            self.display.append(list)
            list=[]
            for j in specs[2].find_all("li"):
                list.append(j.text)
            self.performance.append(list)
            list=[]
            for j in specs[3].find_all("li"):
                list.append(j.text)
            self.connectivity.append(list)
            self.battery.append(np.nan)
            self.others.append(np.nan)
        

    def data_extractor(self):
        containers=self.soup.find_all("div","sm-product has-tag has-features has-actions")
        for i in containers:
            anchor_tags=i.find("a")
            half_link=anchor_tags.get("href")
            link= "https://www.smartprix.com{}".format(half_link)
            self.driver.get(link)
            time.sleep(5)
            self.extractor()
        self.driver.close()

    def convert_to_df(self):
        self.df=pd.DataFrame({
                "name":self.name,
                "price":self.price,
                "ratings":self.ratings,
                "num_rating_reviews":self.num_rating_reviews,
                "general":self.general,
                "display":self.display,
                "performance":self.performance,
                "connectivity":self.connectivity,
                "battery":self.battery,
                
            })
        
    def export_df(self):
        self.df.to_csv(self.config.data_path)

