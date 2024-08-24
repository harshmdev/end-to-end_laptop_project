import pandas as pd
import numpy as np
from src.laptop_ml.entity import MissingValueImputationConfig


class MissingValueImputation:
    def __init__(self, config: MissingValueImputationConfig):
        self.config=config
        self.df=pd.read_csv(self.config.after_cleaning)

    def convert_display_size(self,x):
        if x>11 and x<=14:
            return "small"
        elif x>14 and x<16:
            return "medium"
        else:
            return "large"
        
    def convert_weight(self,x):
        if x<=1.5:
            return "lite"
        elif x>1.5 and x<2.0:
            return "medium"
        else:
            return "heavy"
        
    def thickness_convert(self,x):
        if x<=16:
            return "slim"
        elif x>16 and x<23:
            return "medium"
        else:
            return "thick"
        
    def export_csv(self,df):
        df.to_csv(self.config.filled_data_path)

        
    def missing_value_imputation(self):
        self.df["brand"]=self.df["brand"].str.lower()

        self.df["display_size"]=self.df["display_size"].apply(self.convert_display_size)

        mean_weight=self.df.groupby("display_size")["weight"].mean()

        for i in self.df[self.df["weight"].isnull()].index:
            if self.df.loc[i,"display_size"]=="large":
                self.df.loc[i,"weight"]=mean_weight[0]
            elif self.df.loc[i,"display_size"]=="medium":
                self.df.loc[i,"weight"]=mean_weight[1]
            else:
                self.df.loc[i,"weight"]=mean_weight[2]

        
        self.df["weight"]=self.df["weight"].apply(self.convert_weight)

        mean_thickness=self.df.groupby("weight")["thickness"].mean()

        for i in self.df[self.df["thickness"].isnull()].index:
            if self.df.loc[i,"weight"]=="heavy":
                self.df.loc[i,"thickness"]=mean_thickness[0]
            elif self.df.loc[i,"weight"]=="lite":
                self.df.loc[i,"thickness"]=mean_thickness[1]
            else:
                self.df.loc[i,"thickness"]=mean_thickness[2]

        self.df["thickness"]=self.df["thickness"].apply(self.thickness_convert)

        for i in self.df[self.df["utility"].isnull()].index:
            if self.df.loc[i,"weight"]=="heavy":
                self.df.loc[i,"utility"]="Gaming"
            else:
                self.df.loc[i,"utility"]="Performance"

        for i in self.df[self.df["warranty"].isnull()].index:
            if self.df.loc[i,"price"]<=90000:
                self.df.loc[i,"warranty"]=1
            elif self.df.loc[i,"price"]<=135000:
                self.df.loc[i,"warranty"]=2
            else:
                self.df.loc[i,"warranty"]=3

        for i in self.df[self.df["num_of_cell"].isnull()].index:
            if self.df.loc[i,"price"]<=50000:
                self.df.loc[i,"num_of_cell"]=2
            elif self.df.loc[i,"price"]<=80000:
                self.df.loc[i,"num_of_cell"]=3
            elif self.df.loc[i,"price"]<=150000:
                self.df.loc[i,"num_of_cell"]=4
            else:
                self.df.loc[i,"num_of_cell"]=6

        mean_battery=self.df.groupby("num_of_cell")["battery_capacity"].mean()

        for i in self.df[self.df["battery_capacity"].isnull()].index:
            if self.df.loc[i, "num_of_cell"] == 2.0:
                self.df.loc[i, "battery_capacity"] = mean_battery[2.0]
            elif self.df.loc[i, "num_of_cell"] == 3.0:
                self.df.loc[i, "battery_capacity"] = mean_battery[3.0]
            elif self.df.loc[i, "num_of_cell"] == 4.0:
                self.df.loc[i, "battery_capacity"] = mean_battery[4.0]
            else:
                self.df.loc[i, "battery_capacity"] = mean_battery[6.0]

        for i in self.df["battery_capacity"]:
            if i<=45:
                self.df["battery_capacity"]=self.df["battery_capacity"].replace(i,"low")
            elif i>45 and i<=55:
                self.df["battery_capacity"]=self.df["battery_capacity"].replace(i,"medium")
            elif i>55 and i<=72:
                self.df["battery_capacity"]=self.df["battery_capacity"].replace(i,"high")
            else:
                self.df["battery_capacity"]=self.df["battery_capacity"].replace(i,"very_high")

        self.df["core"].fillna(self.df["core"].mode()[0],inplace=True)

        for i in self.df[self.df["thread"].isnull()].index:
            if self.df.loc[i,"core"]==8:
                self.df.loc[i,"thread"]=16
            elif self.df.loc[i,"core"]==14:
                self.df.loc[i,"thread"]=20
            elif self.df.loc[i,"core"]==6:
                self.df.loc[i,"thread"]=12
            elif self.df.loc[i,"core"]==24:
                self.df.loc[i,"thread"]=32
            elif self.df.loc[i,"core"]==12:
                self.df.loc[i,"thread"]=16
            elif self.df.loc[i,"core"]==10:
                self.df.loc[i,"thread"]=12
            else:
                self.df.loc[i,"thread"]=self.df.loc[i,"core"]

        value=self.df[self.df["cache"]=="Smart Cache Cache"]
        self.df.loc[value.index,"cache"]=np.nan
        self.df["cache"].fillna(self.df["cache"].mode()[0],inplace=True)
        self.df["cache"]=self.df["cache"].astype("float")

        self.df["pixel_height"].fillna(self.df["pixel_height"].mode()[0],inplace=True)
        self.df["pixel_width"].fillna(self.df["pixel_width"].mode()[0],inplace=True)

        val_list=["intel","mediatek","amd","apple"]
        for i in self.df[self.df["processor_gen"].str.lower().isin(val_list)].index:
            if self.df.loc[i,"processor_gen"]=="Apple":
                self.df.loc[i,"processor_gen"]="2nd"
            elif self.df.loc[i,"processor_gen"]=="Intel":
                self.df.loc[i,"processor_gen"]="3rd"
            elif self.df.loc[i,"processor_gen"]=="intel":
                self.df.loc[i,"processor_gen"]="3rd"
            elif self.df.loc[i,"processor_gen"]=="AMD":
                self.df.loc[i,"processor_gen"]="7th"
            elif self.df.loc[i,"processor_gen"]=="MediaTek":
                self.df.loc[i,"processor_gen"]="1st"

        self.df["processor_gen"]=self.df["processor_gen"].str.slice(0,-2)
        self.df["processor_gen"]=self.df["processor_gen"].astype("float")

        for i in self.df["ppi"]:
            if i<=141:
                self.df["ppi"].replace(i,"low",inplace=True)
            elif i<=157:
                self.df["ppi"].replace(i,"medium",inplace=True)
            elif i<=250:
                self.df["ppi"].replace(i,"high",inplace=True)
            else:
                self.df["ppi"].replace(i,"very_high",inplace=True)

        self.df["processor"]=self.df["processor_brand"]+" "+self.df["processor_model"]+" "+self.df["processor_gen"].astype(str)
        self.df["brand"]=self.df["brand"].apply(lambda x:x if self.df["brand"].value_counts()[x]>4 else "others")
        self.df["processor"]=self.df["processor"].apply(lambda x:x if self.df["processor"].value_counts()[x]>6 else "others")
        
        self.export_csv(self.df)
    