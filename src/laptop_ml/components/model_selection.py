import numpy as np
import pandas as pd
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import KFold, cross_val_score
from sklearn.svm import SVR
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler, OrdinalEncoder
from sklearn.compose import ColumnTransformer
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from laptop_ml.entity import ModelSelectionConfig

class ModelSelection:
    def __init__(self,config: ModelSelectionConfig) :
        self.config=config
        self.df=pd.read_csv(self.config.after_feature_selection,index_col=0)

    def prepare_dataset(self,df):
        X = df.drop(columns=['price'])
        y = df['price']
        y_transformed = np.log1p(y)
        return X , y , y_transformed
    
    def export_model(self,pipeline):
        joblib.dump(pipeline,self.config.model_path)
        
    
    def encode_columns(self):
        columns_to_encode=["weight","display_size","battery_capacity","ppi"]
        preprocessor = ColumnTransformer(
            transformers=[
                ('num', StandardScaler(), ["ram","ssd","core","warranty"]),
                ('cat', OrdinalEncoder(), columns_to_encode),
                ('cat1',OneHotEncoder(drop='first'),["brand","utility","graphic","processor"])
            ],
            remainder='passthrough'
        )
        return preprocessor


    def train_model(self):
        X,y,y_transformed=self.prepare_dataset(self.df)
        preprocessor=self.encode_columns()
        pipeline=Pipeline([
            ("preprocessor",preprocessor),
            ("svr",SVR(C=self.config.svr__C,gamma=self.config.svr__gamma, kernel=self.config.svr__kernel))
        ])

        pipeline.fit(X,y_transformed)
        self.export_model(pipeline)


    