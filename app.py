import streamlit as st
import pandas as pd
import sqlite3

conn = sqlite3.connect('kpi.db')

st.title("KPI руководителя")

st.metric("Выручка", pd.read_sql("SELECT SUM(amount) AS v FROM sales", conn).iloc[0,0])
st.metric("Средний чек", pd.read_sql("SELECT AVG(amount) FROM sales", conn).iloc[0,0])

st.subheader("Топ-10 клиентов")
st.dataframe(pd.read_sql(open('queries/top_customers.sql').read(), conn))

st.subheader("Выручка по месяцам")
st.bar_chart(pd.read_sql("""
    SELECT strftime('%Y-%m', sold_at) AS m, SUM(amount) FROM sales GROUP BY m
""", conn).set_index('m'))
