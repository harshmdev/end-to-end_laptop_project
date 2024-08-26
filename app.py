import streamlit as st
from app_modules.price_prediction import price_prediction
from app_modules.analytics_module import AnalyticsModule

analytics=AnalyticsModule()


# HTML code for GitHub and Blog links with icons
html_code = """
<div style="display: flex; align-items: center;">
    <a href="https://github.com/harshmdev/end-to-end_laptop_project.git" target="_blank" style="text-decoration: none; margin-right: 10px;">
        <img src="https://img.icons8.com/ios-glyphs/30/000000/github.png" alt="GitHub" style="vertical-align: middle;">
        GitHub
    </a>
</div>
"""





# Function for each page
def home():
    st.title("Home")
    st.write("Welcome to the Laptop Price Prediction App!")
    st.markdown("""This app is designed to help users predict laptop prices based on various specifications, analyze trends, and explore insights. Below is an overview of the different pages available in the app:""")
    st.markdown("""1. Price Prediction Page->On the Price Prediction Page, you can input the specifications of a laptop—such as RAM, processor, storage, and more—and the app will predict the likely market price for that configuration. This page leverages advanced machine learning models to provide accurate and reliable predictions.
""")
    st.markdown("""2. Analytics Module->The Analytics Module offers insights and visualizations on various trends related to laptop prices. Here, you can explore graphs and charts that reveal how different specifications affect pricing, understand market trends, and make informed decisions based on the data.""")
    st.write("Explore each page to get the most out of this app and make well-informed decisions when it comes to laptop pricing!")
    # Display the HTML code in Streamlit
    st.markdown(html_code, unsafe_allow_html=True)


def analytics_module():
    st.title("Analytics Module")
    analytics.comparison_laptops()
    st.write("<div style='margin: 50px 0;'></div>", unsafe_allow_html=True)
    analytics.price_comparison()
    st.write("<div style='margin: 50px 0;'></div>", unsafe_allow_html=True)
    analytics.corr_matrix()
    st.write("<div style='margin: 50px 0;'></div>", unsafe_allow_html=True)
    analytics.highest_count()




# Sidebar with navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["Home", "Price Prediction", "Analytics Module"])

# Display the selected page
if page == "Home":
    home()
elif page == "Price Prediction":
    price_prediction()
elif page == "Analytics Module":
    analytics_module()

