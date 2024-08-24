import pandas as pd
import numpy as np
from src.laptop_ml.entity import DataCleaningConfig

class DataCleaning:
    def __init__(self,config: DataCleaningConfig) :
        self.config=config
        self.df=pd.read_csv(self.config.preprocessed_data_path)

    def extract_ports(self,port_string):
        usb3 = usb2 = typec = 0
        parts = port_string.split(' x ')
        if len(parts)==2:
            if 'USB 3.0' in parts[1]:
                usb3 = int(parts[0])
            elif 'USB 2.0' in parts[1]:
                usb2 = int(parts[0])
            elif 'Type-C' in parts[1]:
                typec = int(parts[0])
        return pd.Series([usb3, usb2, typec])
    
    def convert_cores(self,core_string):
        if "Cores" in core_string:
            return int(core_string.split(" Cores")[0])
        elif "Quad" in core_string:
            return 4
        elif "Octa" in core_string:
            return 8
        elif "Hexa" in core_string:
            return 6
        elif "Dual" in core_string:
            return 2
        else:
            return np.nan
        
    def extract_processor_brand(self,processor):
        processor=processor.lower()
        if "intel" in processor:
            return "Intel"
        elif "amd" in processor:
            return "AMD"
        elif "apple" in processor:
            return "Apple"
        elif "mediatek" in processor:
            return "Mediatek"
        
    def extract_processor_model(self,processor):
        processor=processor.split()
        if len(processor)>=6:
            return processor[4]
        else :
            return processor[-1]
        
    def extract_processor_generation(self,processor):
        processor=processor.split()
        return processor[0]



    def data_cleaning(self):
        self.df.drop_duplicates(inplace=True)
        self.df['thickness'] = self.df['thickness'].str.split('mm').str[0].str.replace(r"\u2009","").str.strip()
        self.df['weight'] = self.df['weight'].str.split('kg').str[0].str.replace(r"\u2009","").str.strip()
        self.df["warranty"]=self.df["warranty"].str.split().str[0].str.strip().astype(float)
        self.df['display_size'] = self.df['display_size'].str.split('inches').str[0].str.replace(r"\u2009","").str.strip()
        self.df['pixel_width'] = self.df['pixel'].str.split('pixels').str[0].str.split("x").str[0].str.replace(r"\u2009","").str.strip()
        self.df['pixel_height'] = self.df['pixel'].str.split('pixels').str[0].str.split("x").str[1].str.replace(r"\u2009","").str.strip()
        self.df['ppi'] = self.df['ppi'].str.split('PPI').str[0].str.replace(r"\u2009","").str.replace("~","").str.strip()
        self.df["aspect_ratio"]=self.df["aspect_ratio"].str.split("Aspect").str[0].str.strip()
        self.df["ram"]=self.df["ram"].str.split("GB").str[0].str.replace(r"\u2009","").str.strip()
        self.df["hdd"]=self.df["hdd"].str.split("HARD").str[0].str.replace(r"\u2009","").str.strip()
        self.df["ssd"]=self.df["ssd"].str.split("SSD").str[0].str.replace(r"\u2009","").str.strip()
        self.df["cache"]=self.df["cache"].str.split("MB").str[0].str.replace(r"\u2009","").str.strip()
        self.df["thread"]=self.df["thread"].str.replace("Threads","").str.strip()
        self.df["camera"]=self.df["camera"].str.replace(r"\u2009","").str.split("Camera").str[0].str.strip()
        self.df["num_of_cell"]=self.df["num_of_cell"].str.split("Cell").str[0].str.strip()
        self.df["battery_capacity"]=self.df["battery_capacity"].str.split("Battery").str[0].str.replace(r"\u2009Wh","").str.strip()
        self.df.drop("pixel",axis=1, inplace=True)
        self.df.loc[self.df["os"].isnull(),"os"]="Android 11"

        for i in self.df["os"]:
            if "Windows" in i:
                self.df["os"].replace(i,"Windows",inplace=True)
            elif "Mac" in i:
                self.df["os"].replace(i,"Mac",inplace=True)
            else:
                self.df["os"].replace(i,"Others",inplace=True)

        for i in self.df["aspect_ratio"]:
            if i!="16:10" and i!="3:2":
                self.df["aspect_ratio"].replace(i,"16:9",inplace=True)

        for i in self.df["core"]:
            if "Core" in i:
                pass
            else:
                self.df["core"].replace(i,np.nan,inplace=True)

        col_list=["antiglare","touch_screen","hdmi","mcr","bluetooth","backlit_keyboard","inbuilt_microphone","thunderbolt","fingerprint_sensor","ethernet","display_port"]
        for i in col_list:
            self.df[i] = self.df[i].apply(lambda x: 0 if pd.isnull(x) else 1)

        self.df["wifi"]=self.df["wifi"].apply(lambda x:0 if x!="WiFi" else 1)

        self.df["hdd"]=self.df["hdd"].apply(lambda x:"0" if pd.isnull(x) else x)
        for i in self.df["hdd"]:
            if "TB" in i:
                self.df["hdd"].replace(i,i.split("TB")[0],inplace=True)
            elif "GB" in i:
                self.df["hdd"].replace(i,i.split("GB")[0],inplace=True)
            else:
                self.df["hdd"].replace(i,np.nan)


        self.df["hdd"]=self.df["hdd"].astype(int)
        for i in self.df["hdd"]:
            if i<=10:
                self.df["hdd"].replace(i,i*1024,inplace=True)


        self.df["ssd"]=self.df["ssd"].apply(lambda x:"0" if pd.isnull(x) else x)
        for i in self.df["ssd"]:
            if "TB" in i:
                self.df["ssd"].replace(i,i.split("TB")[0],inplace=True)
            elif "GB" in i:
                self.df["ssd"].replace(i,i.split("GB")[0],inplace=True)
        self.df["ssd"]=self.df["ssd"].astype(int)
        for i in self.df["ssd"]:
            if i<=10:
                self.df["ssd"].replace(i,i*1024,inplace=True)


        self.df["graphic"].fillna("Integrated",inplace=True)
        for i in self.df["graphic"]:
            if "NVIDIA" in i:
                self.df["graphic"].replace(i,"NVIDIA",inplace=True)
            elif "AMD" in i:
                self.df["graphic"].replace(i,"AMD",inplace=True)
            else:
                self.df["graphic"].replace(i,"Integrated",inplace=True)

        self.df["camera"]=self.df["camera"].str.replace("MP","").str.strip()

        self.df["usb"].fillna("0x0",inplace=True)

        self.df[["usb3", "usb2", "type_c"]] = self.df["usb"].apply(self.extract_ports)

        self.df["core"].fillna("",inplace=True)

        self.df["core"]=self.df["core"].apply(self.convert_cores)

        self.df["processor_brand"]=self.df["processor"].apply(self.extract_processor_brand)

        self.df["processor_model"]=self.df["processor"].apply(self.extract_processor_model)

        self.df["processor_model"].replace("Chip","M2",inplace=True)
        self.df["processor_model"].replace("Pro","M2",inplace=True)
        self.df["processor_model"].replace("Max","M2",inplace=True)
        self.df["processor_model"].replace("Silver","3050U",inplace=True)

        self.df["processor_gen"]=self.df["processor"].apply(self.extract_processor_generation)

        self.df.drop(columns=["processor","usb"],inplace=True)

        self.df.to_csv(self.config.cleaned_data_path,index=False)

