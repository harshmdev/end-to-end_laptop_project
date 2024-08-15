import pandas as pd
import numpy as np
from laptop_ml.entity import DataPreprocessingConfig




class DataPreprocessing:
    def __init__(self, config: DataPreprocessingConfig):
        self.config=config
        self.df=pd.read_csv(config.raw_data_path,index_col=0)

    def extract_attribute(self,attr_list, keyword):
        for attr in attr_list:
            if keyword in attr:
                return attr.strip()
        return None
     
    # Function to extract a specific attribute from the 'general' column
    def extract_general_attribute(self,attr_list, keyword):
        for attr in attr_list:
            if keyword in attr:
                return attr.split(':')[-1].strip()
        return None
    
    def weight_extractor(self,attr_list):
        for attr in attr_list:
            if 'kg' in attr:
                return attr
        return None
    
    def extract_processor(self,attr_list):
        if attr_list is not None:
            return attr_list[0]
        return None

    def extract_cores(self,attr_list):
        if attr_list is not None:
            return attr_list[2]
        return None

    def data_preprocessing(self):
        # Extract the brand from the 'name' column
        self.df['brand'] = self.df['name'].str.split().str[0]
        
        # Remove the rupee sign and commas, then convert to numeric
        self.df['price'] = self.df['price'].str.replace('₹', '').str.replace(',', '').astype(float)

        # Extract the number of votes by splitting the string
        self.df['no_of_votes'] = self.df['ratings'].str.split().str[0].str.replace(',', '').astype(int)

        # Extract the ratings by splitting the string and removing unnecessary parts
        self.df['rating'] = self.df['num_rating_reviews'].str.split(':').str[-1].str.replace(';', '').astype(float)

        # Convert the 'general' column strings into lists
        self.df['general_list'] = self.df['general'].str.strip("[]").str.replace("'", "").str.split(',')
        self.df["display_list"]=self.df["display"].str.strip("[]").str.replace("'","").str.split(",")
        self.df["performance_list"]=self.df["performance"].str.strip("[]").str.replace("'","").str.split(",")
        self.df["connectivity_list"]=self.df["connectivity"].str.strip("[]").str.replace("'","").str.split(",")
        self.df["battery_list"] = self.df["battery"].apply(lambda x: x.strip("[]").replace("'", "").split(",") if isinstance(x, str) else [])

        # Extract attributes into separate columns
        self.df['os'] = self.df['general_list'].apply(lambda x: self.extract_general_attribute(x, 'OS'))
        self.df['utility'] = self.df['general_list'].apply(lambda x: self.extract_general_attribute(x, 'Utility'))
        self.df['thickness'] = self.df['general_list'].apply(lambda x: self.extract_general_attribute(x, 'Thickness'))
        self.df['weight'] = self.df['general_list'].apply(lambda x: self.weight_extractor(x) )
        self.df['warranty'] = self.df['general_list'].apply(lambda x: self.extract_general_attribute(x, 'Warranty'))    
        self.df["display_size"]=self.df["display_list"].apply(lambda x:self.extract_attribute(x,"inches"))
        self.df["pixel"]=self.df["display_list"].apply(lambda x:self.extract_attribute(x,"pixels"))
        self.df["ppi"]=self.df["display_list"].apply(lambda x:self.extract_attribute(x,"PPI"))
        self.df["aspect_ratio"]=self.df["display_list"].apply(lambda x:self.extract_attribute(x,"Aspect"))
        self.df["antiglare"]=self.df["display_list"].apply(lambda x:self.extract_attribute(x,"Anti"))
        self.df["touch_screen"]=self.df["display_list"].apply(lambda x:self.extract_attribute(x,"Touch"))
        self.df["ram"]=self.df["performance_list"].apply(lambda x:self.extract_attribute(x,"RAM"))
        self.df["hdd"]=self.df["performance_list"].apply(lambda x:self.extract_attribute(x,"HARD"))
        self.df["ssd"]=self.df["performance_list"].apply(lambda x:self.extract_attribute(x,"SSD"))
        self.df["graphic"]=self.df["performance_list"].apply(lambda x:self.extract_attribute(x,"Graphics"))
        self.df["cache"]=self.df["performance_list"].apply(lambda x:self.extract_attribute(x,"Cache"))
        self.df["thread"]=self.df["performance_list"].apply(lambda x:self.extract_attribute(x,"Threads"))
        self.df["processor"]=self.df["performance_list"].apply(lambda x:self.extract_processor(x))
        self.df["core"]=self.df["performance_list"].apply(lambda x:self.extract_cores(x))
        self.df["hdmi"]=self.df["connectivity_list"].apply(lambda x:self.extract_attribute(x,"HDMI"))
        self.df["mcr"]=self.df["connectivity_list"].apply(lambda x:self.extract_attribute(x,"Multi"))
        self.df["wifi"]=self.df["connectivity_list"].apply(lambda x:self.extract_attribute(x,"WiFi"))
        self.df["bluetooth"]=self.df["connectivity_list"].apply(lambda x:self.extract_attribute(x,"Bluetooth"))
        self.df["usb"]=self.df["connectivity_list"].apply(lambda x:self.extract_attribute(x,"USB"))
        self.df["backlit_keyboard"]=self.df["connectivity_list"].apply(lambda x:self.extract_attribute(x,"Backlit"))
        self.df["inbuilt_microphone"]=self.df["connectivity_list"].apply(lambda x:self.extract_attribute(x,"Microphone"))
        self.df["thunderbolt"]=self.df["connectivity_list"].apply(lambda x:self.extract_attribute(x,"Thunderbolt"))
        self.df["fingerprint_sensor"]=self.df["connectivity_list"].apply(lambda x:self.extract_attribute(x,"Fingerprint"))
        self.df["ethernet"]=self.df["connectivity_list"].apply(lambda x:self.extract_attribute(x,"Ethernet"))
        self.df["display_port"]=self.df["connectivity_list"].apply(lambda x:self.extract_attribute(x,"Display"))
        self.df["camera"]=self.df["connectivity_list"].apply(lambda x:self.extract_attribute(x,"Camera"))
        self.df["num_of_cell"]=self.df["battery_list"].apply(lambda x:self.extract_attribute(x,"Cell"))
        self.df["battery_capacity"]=self.df["battery_list"].apply(lambda x:self.extract_attribute(x,"Wh"))

        self.df.drop(columns=["ratings", "num_rating_reviews", "general","general_list","display","display_list","performance","performance_list","connectivity","connectivity_list","battery","battery_list"] , inplace=True)

        
    def export_preprocessed_data(self):
        self.df.to_csv(self.config.preprocessed_data_path , index=False)