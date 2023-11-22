import streamlit as st
import pandas as pd
import pymongo

MONGO_DETAILS = "mongodb://TGR_GROUP16:ED370J@mongodb:27017"

st.set_page_config(
    page_title = "House Rent Dashboard",
    page_icon = ":bar_chart:",
    layout = "wide"
)

@st.cache_resource
def init_connection():
     return pymongo.MongoClient(MONGO_DETAILS)

client = init_connection()

@st.cache_data
def get_data():
     db = client.mockupdata
     data = db.waterdata.find()
     df = pd.DataFrame(data = data, columns = ["Name", "Date", "Month", "Year", "waterDataFront", "WaterDataBack", "WaterDrainRate"])
     return df

st.markdown("# Another page bite the dust")
st.sidebar.markdown("* Another page")

df = get_data()
st.dataframe(df) 

st.button("calculate", key = "calculate")
st.divider()

left_column, right_column = st.columns(2)

with left_column:
    left_cal_container = st.empty()

with right_column:
        right_cal_container = st.empty()

if (st.session_state.calculate):
    avg_rent = round(df['Rent'].mean(), 1)
    st.write("Average rent is ", str(avg_rent))

if (st.session_state.calculate):
    avg_size = round(df['Size'].mean(), 2)
    st.write("Average size is", str(avg_size))

if (st.session_state.calculate):
     st.divider()

choice_column, display_column = st.columns(2)
with choice_column:         
    st.button("area chart", key = "area_chart")
    st.button("bar chart", key = "bar_chart")
    st.button("line chart", key = "line_chart")
    
with display_column:
    container = st.empty()
    container.text("Select kind of Chart you would like to see")
         
         
if (st.session_state.area_chart):
    container.area_chart(data = df, x = "Size", y = "Rent")
elif (st.session_state.bar_chart):
    container.bar_chart(data = df, x = "Size", y = "Rent")
elif (st.session_state.line_chart):
    container.line_chart(data = df, x = "Size", y = "Rent")

