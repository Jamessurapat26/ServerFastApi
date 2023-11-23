from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st


colTitle1,colTitle2,colTitle3 = st.columns([1,3,1])
colTitle2.title("กราฟแสดงระดับน้ำ")
df = pd.read_csv("Q1A.csv")
df = pd.DataFrame(df)

day_df = df['Day']

col1 , col2 , col3 = st.columns(3)

# Use different variable names for the select boxes
start_day = col1.selectbox('วันเริ่มต้น', day_df)
end_day = col2.selectbox('วันสุดท้าย', day_df, index = (day_df.size-1))

col1 , col2 , col3 = st.columns(3)
with col1:
    st.write('You selected start day:', start_day)
with col2:
     st.write('You selected end day:', end_day)

# Filter the DataFrame based on the selected start and end days
filtered_df = df[(df['Day'] >= start_day) & (df['Day'] <= end_day)]

filtered_df['Modified_Height'] = (120 - filtered_df['Height_S1'])

# Display the bar chart
st.bar_chart(filtered_df[['Day', 'Modified_Height']].set_index('Day'))

st.experimental_set_query_params(
    show_map=True,
    selected=["asia", "america"],
)

# on = st.toggle('Advance Data')




# @st.cache_data
# def convert_df(df):
#     # IMPORTANT: Cache the conversion to prevent computation on every rerun
#     return df.to_csv().encode('utf-8')

# if on:

#     st.dataframe(df,width=700)

    
#     st.line_chart(df[['Discharge_S1', 'Discharge_S2', 'Discharge_S3']])

#     st.write('เปรียบเทียบอัตราการไหล')

#     col1,col2 = st.columns([1,4])
#     with col1:
#         option1 = st.selectbox("Select the first option", ('S1', 'S2', 'S3'))
#         option2 = st.selectbox("Select the second option", ('S1', 'S2', 'S3'))

#     # Assign the selected columns to variables
#     if option1 == 'S1':
#         o1 = df['Discharge_S1']
#     elif option1 == 'S2':
#         o1 = df['Discharge_S2']
#     elif option1 == 'S3':
#         o1 = df['Discharge_S3']

#     if option2 == 'S1':
#         o2 = df['Discharge_S1']
#     elif option2 == 'S2':
#         o2 = df['Discharge_S2']
#     elif option2 == 'S3':
#         o2 = df['Discharge_S3']

#     # Line chart with selected columns
#     col2.line_chart(pd.concat([o1, o2], axis=1))

#     # show_chart = st.radio("Show or hide chart", ["Show Chart", "Hide Chart"])
#     # if show_chart == "Show Chart":
#     #     st.line_chart(df[['Discharge_S1', 'Discharge_S2', 'Discharge_S3']])
#     # else:
#     #     st.write("Chart is hidden.")


#     csv = convert_df(df)

#     st.download_button(
#         label="Download data as CSV",
#         data=csv,
#         file_name='Q1A.csv',
#         mime='waterdata.csv',
#     )










