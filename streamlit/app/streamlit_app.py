from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

st.title("TEST")
st.header("Header")
st.subheader("subheader")
st.text("Hello, world!")
st.slider(label = "progress slider", key = "progress_slider")
st.progress(value = st.session_state.progress_slider, text = "progress bar")