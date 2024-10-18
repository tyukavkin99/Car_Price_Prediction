import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import joblib
import pickle
import json
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor

# Text for analysis
text_for_analysis_boxplot_1 = '''From the boxplot presented, we can see that the distributions of brands' prices are similar, 
                                which means that brand may not be an important feature 
                                for prediction of the prices.

As for the analysis, it surprises as the luxury cars and more middle class cars have 
                                similar distributions'''

# Text for modelling
text_for_modeling = '''The possible models to use: 
                        - Linear Regression 
                        - Random Forrest Regressor 
                        - AdaBoost Regressor'''

def remove_id_column(dataset:pd.DataFrame):
    dataset = dataset.drop(columns=["Car ID"])
    return dataset

def create_boxplot_brands(df:pd.DataFrame):
    fig = px.box(df, x="Brand", y="Price")
    return fig

def create_boxplot_models(df:pd.DataFrame):
    fig = px.box(df, x="Model", y="Price")
    return fig

def create_treemap(df):
    brand_cond_model_price_med = df.groupby(["Brand","Model","Condition"])["Price"].median().reset_index()
    tree = px.treemap(brand_cond_model_price_med, path=["Brand","Model","Condition"], values="Price", color="Price", color_continuous_scale='RdBu')
    return tree

def main():
    st.set_page_config(layout="wide")
    st.title("Car Price Analysis and Prediction")
    df = pd.read_csv("car_price_prediction_.csv", parse_dates=["Year"])
    col1, col2 = st.columns(2)
    with col1:
        st.header("Features")
        st.write(pd.DataFrame({"features":df.columns}))
    with col2:
        st.header("Sample of the dataset")
        df = remove_id_column(df)
        st.write(df.head(10))
    
    st.header("Analysis")
    st.markdown(text_for_analysis_boxplot_1)
    st.plotly_chart(create_boxplot_brands(df=df), use_container_width=True)
    st.plotly_chart(create_boxplot_models(df=df), use_container_width=True)
    st.plotly_chart(create_treemap(df=df), use_container_width=True)

    st.header("Modelling")
    st.markdown(text_for_modeling)

    col3, col4, col5, col6, col7, col8, col9, col10 = st.columns(8)

    with col3:
        brand = st.text_input("Insert the brand name: ")
        st.write("The brand name is: ", brand)
    with col4:
        year = st.number_input("Insert the year: ")
        st.write("The current year is: ", year)
    with col5:
        engine = st.number_input("Insert engine size: ")
        st.write("The engine size is: ", engine)
    with col6:
        fuel = st.text_input("Insert fuel type: ")
        st.write("The fuel type is: ", fuel)
    with col7:
        transmission = st.text_input("Insert transmission: ")
        st.write("The transmission is: ", transmission)
    with col8:
        mileage = st.number_input("Insert the mileage: ")
        st.write("The mileage is: ", mileage)
    with col9:
        model_name = st.text_input("Insert the model name: ")
        st.write("The model name is: ", model_name)
    with col10:
        condition = st.text_input("Insert condition: ")
        st.write("The current condition is: ", condition)


if __name__ == "__main__":
    main()
