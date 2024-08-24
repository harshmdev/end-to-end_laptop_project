import streamlit as st
import pandas as pd
from laptop_ml.pipeline.price_prediction import PredictionPipeline

prediction_pipeline=PredictionPipeline()

def price_prediction():
    df=pd.read_csv("artifacts/feature_selection/after_feature_selection.csv")
    st.title("Price Prediction")
    st.write("Please enter your inputs for price prediction")
    col1, col2 = st.columns(2)

    with col1:
        select_brand = st.selectbox("Select Brand", sorted(df["brand"].unique().tolist()))
        select_utility = st.selectbox("Utility", df["utility"].unique())
        select_weight = st.selectbox("Weight", df["weight"].unique())
        select_warranty = float(st.selectbox("Warranty", df["warranty"].unique()))
        select_display = st.selectbox("Display Size", df["display_size"].unique())
        select_ppi = st.selectbox("PPI", df["ppi"].unique())

    with col2:
        select_ram = float(st.selectbox("RAM", sorted(df["ram"].unique().tolist())))
        select_ssd = float(st.selectbox("SSD", sorted(df["ssd"].unique().tolist())))
        select_core = float(st.selectbox("No. of Cores", sorted(df["core"].unique().tolist())))
        select_graphic = st.selectbox("Graphic Brand", df["graphic"].unique())
        select_battery_capacity = st.selectbox("Battery Capacity", df["battery_capacity"].unique())
        select_processor = st.selectbox("Processor", sorted(df["processor"].unique().tolist()))

    # Additional checkboxes in a row
    col3, col4, col5 = st.columns(3)
    
    with col3:
        if st.checkbox("Touch Screen"):
            touchscreen=1
        else:
            touchscreen=0
        
    with col4:
        if st.checkbox("HDMI"):
            hdmi=1
        else:
            hdmi=0
        
    with col5:

        if st.checkbox("Backlit Keyboard"):
            backlit=1
        else:
            backlit=0

    if st.button("Predict"):
        #Make a dataframe
        columns=['brand', 'utility', 'weight', 'warranty', 'display_size', 'ppi',
       'touch_screen', 'ram', 'ssd', 'graphic', 'core', 'hdmi',
       'backlit_keyboard', 'battery_capacity', 'processor']
        data=[[select_brand,select_utility,select_weight,select_warranty,select_display,select_ppi,touchscreen,select_ram,select_ssd,select_graphic,select_core,hdmi,backlit,select_battery_capacity,select_processor]]
        df=pd.DataFrame(data,columns=columns)

        #predict
        output=prediction_pipeline.predict(df=df)
        lower_range=int((output-0.10*output).round()[0])
        upper_range=int((output+0.10*output).round()[0])

        #display
        st.write("The Price of laptop ranges between  {}  to  {} ".format(lower_range,upper_range))