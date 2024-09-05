import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.title("🎈 Read Google Sheet as DataFrame")

conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read(worksheet="Daily Metrics")

st.dataframe(df)