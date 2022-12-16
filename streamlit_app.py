import streamlit as st
import pandas as pd

st.header('Netflix Data Visualizer by Country')

netflix = pd.read_csv("https://raw.githubusercontent.com/practiceprobs/datasets/main/netflix-titles/netflix-titles.csv")

filter_options = list()
for column_name in netflix.columns:
    if column_name not in ['country', 'title']:
        filter_options.append(column_name)


def visualize_data(y_axis):
    chart_data = pd.DataFrame(netflix)
    st.bar_chart(chart_data, x='country', y=y_axis)


option = st.selectbox('Filter', filter_options)

st.button('Generate Visualization', on_click=visualize_data(option))