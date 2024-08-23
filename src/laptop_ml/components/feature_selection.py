import pandas as pd
from laptop_ml.entity import FeatureSelectionConfig

class FeatureSelection:
    def __init__(self, config: FeatureSelectionConfig):
        self.config=config
        self.df=pd.read_csv(self.config.after_missing_value_imputation)

    def export_csv(self,df):
        df.to_csv(self.config.selected_data_path,index=False)


    def feature_selection(self):
        export_df = self.df.drop(columns=["processor_brand","processor_model","processor_gen","thread","name","no_of_votes","rating","camera","thickness","usb3","bluetooth","inbuilt_microphone","usb2","hdd","display_port","pixel_width","pixel_height","thunderbolt","wifi","ethernet","num_of_cell","mcr","os","antiglare","type_c","fingerprint_sensor","aspect_ratio","cache"])
        self.export_csv(export_df)