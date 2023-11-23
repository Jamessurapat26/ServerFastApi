from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st


colTitle1,colTitle2,colTitle3 = st.columns([1,6,1])
colTitle2.title("กราฟแสดงอัตราการไหล")
df = pd.read_csv("Q1A.csv")
df = pd.DataFrame(df)

@st.cache_data
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

# st.dataframe(df,width=700)

st.write("\n")
st.write("\n")
st.write("\n")

    
st.line_chart(df[['Discharge_S1', 'Discharge_S2', 'Discharge_S3']])

colh1,colh2,colh3 = st.columns([1,3,1])

colh2.header('เปรียบเทียบอัตราการไหล')
st.write("\n")
st.write("\n")

col1,col2 = st.columns([1,4])
with col1:
    option1 = st.selectbox("Select Station", ('Station 1', 'Station 2', 'Station 3'))
    option2 = st.selectbox("Select Station.", ('Station 1', 'Station 2', 'Station 3'))

    # Assign the selected columns to variables
if option1 == 'Station 1':
        o1 = df['Discharge_S1']
elif option1 == 'Station 2':
        o1 = df['Discharge_S2']
elif option1 == 'Station 3':
        o1 = df['Discharge_S3']

if option2 == 'Station 1':
        o2 = df['Discharge_S1']
elif option2 == 'Station 2':
        o2 = df['Discharge_S2']
elif option2 == 'Station 3':
        o2 = df['Discharge_S3']

    # Line chart with selected columns
col2.line_chart(pd.concat([o1, o2], axis=1))

    # show_chart = st.radio("Show or hide chart", ["Show Chart", "Hide Chart"])
    # if show_chart == "Show Chart":
    #     st.line_chart(df[['Discharge_S1', 'Discharge_S2', 'Discharge_S3']])
    # else:
    #     st.write("Chart is hidden.")


csv = convert_df(df)

st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name='Q1A.csv',
        mime='waterdata.csv',
)



