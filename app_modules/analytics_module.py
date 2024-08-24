import streamlit as st
import pandas as pd
import plotly.express as px

class AnalyticsModule:
    def __init__(self) -> None:
        self.df=pd.read_csv("artifacts/missing_value_imputation/after_missing_value_imputation.csv",index_col=0)
        self.df1=pd.read_csv("artifacts/data_cleaning/cleaned_data.csv",index_col=0)

    def comparison_laptops(self):
        st.subheader("Comparison between laptops")
        col1,col2=st.columns(2)
        with col1:
            laptop1=st.selectbox("Laptop 1",sorted(self.df["name"].tolist()))
            row1=self.df[self.df["name"]==laptop1]
            st.write("Price",row1.iloc[0]["price"])
            st.write("Votes",row1.iloc[0]["no_of_votes"])
            st.write("Rating",row1.iloc[0]["rating"])
            st.write("Utility: ",row1.iloc[0]["utility"])
            st.write("RAM",row1.iloc[0]["ram"])
            st.write("SSD",row1.iloc[0]["ssd"])
            st.write("Graphic: ",row1.iloc[0]["graphic"])
            st.write("Processor: ",row1.iloc[0]["processor"])
            

        with col2:
            laptop2=st.selectbox("Laptop 2",sorted(self.df["name"].tolist()))
            row2=self.df[self.df["name"]==laptop2]
            st.write("Price",row2.iloc[0]["price"])
            st.write("Votes",row2.iloc[0]["no_of_votes"])
            st.write("Rating",row2.iloc[0]["rating"])
            st.write("Utility: ",row2.iloc[0]["utility"])
            st.write("RAM",row2.iloc[0]["ram"])
            st.write("SSD",row2.iloc[0]["ssd"])
            st.write("Graphic: ",row2.iloc[0]["graphic"])
            st.write("Processor: ",row2.iloc[0]["processor"])

    def price_comparison(self):
        st.subheader("Relation of price with other features")
        feature=st.selectbox("Feature List",["brand" , "utility" , "weight", "thickness" ,"ppi","graphic","processor_brand","ram","ssd","core"])
        feature_value=self.df.groupby(feature)["price"].mean().sort_values(ascending=False)
        fig=px.bar(self.df,x=feature_value.index,y=feature_value , title='Price vs {}'.format(feature))
        fig.update_layout(
            xaxis_title=feature,
            yaxis_title="Price"
        )
        st.plotly_chart(fig,use_container_width=True)

    def corr_matrix(self):
        st.subheader("Correlation Matrix")
        numerical=["price","no_of_votes","rating","thickness","weight","display_size","ppi","battery_capacity","ram","hdd","ssd","thread","core","num_of_cell","usb3","usb2","type_c"]
        fig=px.imshow(self.df1[numerical].corr())
        fig.update_layout(
            autosize=False,
            width=800,  # Adjust width as needed
            height=600,
            margin=dict(l=0, r=0, b=0, t=0, pad=4),  # Adjust height as needed
            coloraxis_colorbar=dict(
            thicknessmode="pixels", thickness=20,
            lenmode="pixels", len=500,
            yanchor="middle", y=0.5,
            xanchor="right", x=1.2
        )
        )
        st.plotly_chart(fig)

    def highest_count(self):
        st.subheader("Value Count of Discrete Numerical Features")
        feature=st.selectbox("select column",["ram","ssd","warranty","core","ppi"])
        feature_count=self.df[feature].value_counts().sort_values(ascending=False).reset_index()
        feature_count.columns = [feature, 'count']
        fig = px.bar(feature_count, x=feature, y='count', title=f"Most common {feature}")        
        fig.update_layout(
            autosize=False,
            width=800,  # Adjust width as needed
            height=600,
            xaxis_title=feature,
            yaxis_title="Value Count"
        )
        st.plotly_chart(fig,use_container_width=True)


