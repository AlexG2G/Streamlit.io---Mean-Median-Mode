import pandas as pd
import streamlit as st

#Mean

list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
mean = sum(list1)/len(list1)

list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
list1.sort()

#Median

if len(list1) % 2 == 0:
    m1 = list1[len(list1)//2]
    m2 = list1[len(list1)//2 - 1]
    median = (m1 + m2)/2
else:
    median = list1[len(list1)//2]

#Mode

    list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
frequency = {}
for i in list1:
    frequency.setdefault(i, 0)
    frequency[i]+=1

frequent = max(frequency.values())
for i, j in frequency.items():
    if j == frequent:
        mode = i


@st.cache(suppress_st_warning=True)
def read_data(path):
    return pd.read_csv(path)

def head():
    st.markdown("""
        <h1 style='text-align: center; margin-bottom: -35px;'>
        Mean, Median and Mode calculator for a list of integers.
        </h1>
    """, unsafe_allow_html=True
    )
    
    st.caption("""
        <p style='text-align: center'>
        by <a href='https://thecleverprogrammer.com/2022/03/31/mean-median-and-mode-using-python/'>Mean Median and Mode using Python</a>
        </p>
    """, unsafe_allow_html=True
    )
    
    st.write(
        "Click the button to generate the Mean, Median and Mode for the Dataset \U0001F642."
        " [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]."
    )


def body(sample): 
    st.write(mean)
    st.write(median)
    st.write(mode)
    st.markdown('---')