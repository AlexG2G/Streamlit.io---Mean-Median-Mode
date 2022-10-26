import pandas as pd
import streamlit as st

@st.cache(suppress_st_warning=True)
def read_data(path):
    return pd.read_csv(path)