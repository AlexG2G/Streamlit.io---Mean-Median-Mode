import pandas as pd
import streamlit as st
from utils import read_data, head, body

st.set_page_config(
    page_title='Mean, Median and Mode Calculator',
)
 
head()

if st.button('Calculate Mean, Median and Mode for the Dataset'):
    df = read_data('list1.csv')
    choice = df.sample(10)
    body(choice)
    st.write(df)
