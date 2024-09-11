import streamlit as st
from streamlit_gsheets import GSheetsConnection


st.title("🎈 Read Google Sheet as DataFrame")

conn_hm = st.connection("healthmetrics", type=GSheetsConnection)
df_hm = conn_hm.read(worksheet="Daily Metrics")

st.dataframe(df_hm)

conn_wo = st.connection("workouts", type=GSheetsConnection)
df_wo = conn_wo.read(worksheet="Workouts")

st.dataframe(df_wo)