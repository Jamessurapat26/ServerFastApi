import streamlit as st
import pandas as pd
import pymongo
from datetime import date

MONGO_DETAILS = "mongodb://TGR_GROUP16:ED370J@mongodb:27017"

st.set_page_config(
    page_title = "ข้อมูลระดับน้ำ",
    page_icon = ":bar_chart:",
    layout="centered"
)

@st.cache_resource
def init_connection():
     return pymongo.MongoClient(MONGO_DETAILS)

client = init_connection()

@st.cache_data
def get_data():
     db = client.mockupdata
     data = db.waterdata.find()
     send_data = list(data)
     df = []
    #  temp_df = pd.DataFrame(data = data, columns = ["Name", "Date", "Month", "Year", "WaterDataFront", "WaterDataBack", "WaterDrainRate"])
     for temp_data in send_data:
          fulldate = date(temp_data["Year"], temp_data["Month"], temp_data["Date"])
          data = {
               "Name": temp_data["Name"],
               "Fulldate": date(temp_data["Year"], temp_data["Month"], temp_data["Date"]),
               "Date": fulldate.day,
               "Month": fulldate.month,
               "Year": fulldate.year,
               "WaterDataFront": float(temp_data["WaterDataFront"]),
               "WaterDataBack": float(temp_data["WaterDataBack"]),
               "WaterDrainRate": float(temp_data["WaterDrainRate"]),

          }
          df.append(data)
     print(df)
     return df

st.title("ข้อมูลระดับน้ำ")
st.sidebar.markdown("* Water data")

df = pd.DataFrame(data = get_data())

month_list = {
     "มกราคม": 1,
     "กุมภาพันธ์": 2,
     "มีนาคม": 3,
     "เมษายน": 4,
     "พฤษภาคม": 5,
     "มิถุนายน": 6,
     "กรกฎาคม": 7,
     "สิงหาคม": 8,
     "กันยายน": 9,
     "ตุลาคม": 10,
     "พฤศจิกายน": 11,
     "ธันวาคม": 12
}

year_list = range(2016, 2024)


st.subheader("กรุณาเลือกเดือนและปีที่ต้องการดูข้อมูล")
selected_month = st.selectbox("เดือน", options = month_list)
selected_year = st.selectbox("ปี", options = year_list )

temp = df.loc[(df['Month'] == month_list[selected_month]) & (df['Year'] == selected_year)]
max_WDF = temp.sort_values('WaterDataFront', ascending=False).head(1)
max_WDB = temp.sort_values('WaterDataBack', ascending=False).head(1)

col1, col2 = st.columns(2)
col1.metric("ระดับน้ำสูงสุดบริเวณหน้าเขื่อน", value = max_WDF['WaterDataFront'])
col2.metric("ระดับน้ำสูงสุดบริเวณหลังเขื่อน", value = max_WDB['WaterDataBack'])

left_column, right_column = st.columns(2)

with left_column:
    st.write("ระดับน้ำบริเวณหน้าเขื่อน")
    st.bar_chart(data = df.loc[(df['Month'] == month_list[selected_month]) & (df['Year'] == selected_year)], x = 'Date', y = "WaterDataFront", color = "#41AAA8")

with right_column:
    st.write("ระดับน้ำบริเวณหลังเขื่อน")
    st.bar_chart   (data = df.loc[(df['Month'] == month_list[selected_month]) & (df['Year'] == selected_year)], x = 'Date', y = "WaterDataBack", color = "#41AAA8")

st.write("อัตราการระบายน้ำ")
st.line_chart(data = df.loc[(df['Month'] == month_list[selected_month]) & (df['Year'] == selected_year)], x = 'Date', y = "WaterDrainRate", color = "#41AAA8")

st.subheader("ข้อมูลน้ำทั้งหมด")
st.dataframe(df[['Name', 'Fulldate', 'WaterDataFront', 'WaterDataBack', 'WaterDrainRate']], use_container_width = True, hide_index = True)