import streamlit as st
import joblib
import pandas as pd
import numpy as np
from app_modules.price_prediction import price_prediction
from app_modules.analytics_module import AnalyticsModule

analytics=AnalyticsModule()


# Function for each page
def home():
    st.title("Home")
    st.write("Welcome to the Home page!")



def analytics_module():
    analytics.comparison_laptops()
    st.write("<div style='margin: 50px 0;'></div>", unsafe_allow_html=True)
    analytics.price_comparison()
    st.write("<div style='margin: 50px 0;'></div>", unsafe_allow_html=True)
    analytics.corr_matrix()
    st.write("<div style='margin: 50px 0;'></div>", unsafe_allow_html=True)
    analytics.highest_count()



def insight_module():
    st.title("Insight Module")
    st.write("This is the Insight Module page.")

# Sidebar with navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["Home", "Price Prediction", "Analytics Module", "Insight Module"])

# Display the selected page
if page == "Home":
    home()
elif page == "Price Prediction":
    price_prediction()
elif page == "Analytics Module":
    analytics_module()
elif page == "Insight Module":
    insight_module()
