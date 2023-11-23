from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st



df = pd.read_csv("Q1A.csv")

colTitle1,colTitle2,colTitle3 = st.columns([1,4,1])
colTitle2.title("เว็บไซต์แสดงระดับน้ำ")
st.write("\n")


max_height = df['Height_S1'].max()
min_height = df['Height_S1'].min()
a = 10
b = 20

# st.button("แสดงระดับน้ำปัจจุบัน", type="primary")
container = st.empty

if st.button("แสดงระดับน้ำปัจจุบัน" , type="primary"):
    current_height = df.Height_S1.iloc[-1]
else:
    # แสดงระดับน้ำตรงกลางตารางข้อมูลของสถานี S1 
    current_height = df.Height_S1.iloc[int(df['Height_S1'].size / 2)]

col_current1,col_current2,col_current3 = st.columns(3)

with col_current2:
    st.metric(label="ระดับปัจจุบัน", value=f"{current_height} เมตร", delta="1.2 เมตร")

st.write("\n")
st.divider()
st.write("\n")
st.write("\n")

col1, col2 = st.columns(2)
with col1:
    st.metric("ระดับน้ำสูงสุด", f"{max_height} เมตร", "")
with col2:
    st.metric("ระดับน้ำต่ำสุด", f"{min_height} เมตร", "")




