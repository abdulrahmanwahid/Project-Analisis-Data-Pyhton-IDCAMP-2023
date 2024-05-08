import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import seaborn as sns
import streamlit as st
import urllib
from func import DataAnalyzer, BrazilMapPlotter
from babel.numbers import format_currency
sns.set(style='dark')
st.set_option('deprecation.showPyplotGlobalUse', False)

# Dataset
datetime_cols = ["order_approved_at", "order_delivered_carrier_date", "order_delivered_customer_date", "order_estimated_delivery_date", "order_purchase_timestamp", "shipping_limit_date"]
all_df = pd.read_csv("./dataset/all_data.csv")
all_df.sort_values(by="order_approved_at", inplace=True)
all_df.reset_index(inplace=True)

# Geolocation Dataset
geolocation = pd.read_csv("./dataset/geolocation.csv")
data = geolocation.drop_duplicates(subset='customer_unique_id')

for col in datetime_cols:
    all_df[col] = pd.to_datetime(all_df[col])

min_date = all_df["order_approved_at"].min()
max_date = all_df["order_approved_at"].max()

with st.container():
  left_col, right_col = st.columns(2)
  
  with left_col:
    st.subheader('E-Commerce Pubilc Dataset Analysis')
    st.title("Hi, Guys I'm Wahid :wave:")
    st.markdown(
      """I'm an Informatics Engineering student at Universitas Lampung.""")
    
  # Logo Image
    st.image("./dashboard/logo.png")

    # Date Range
    start_date, end_date = st.date_input(
        label="Select Date Range",
        value=[min_date, max_date],
        min_value=min_date,
        max_value=max_date
    )
    
with st.container():
  st.write("---")
  st.subheader("Apakah lokasi para seller tersebar merata di setiap state?")

  fig, ax = plt.subplots(figsize=(16, 8))
  sns.barplot(y=state_df['State'], x=state_df['Count'], orient='h', color='#1F9ED1')
  ax.set_ylabel("State", fontsize=14)
  ax.set_xlabel(None)
  ax.set_title("Population of Seller in Each State", loc="center", fontsize=17)
  
  st.pyplot(fig)

  with st.expander("See answer"):
    st.write("""Tidak, para seller belum tersebar secara merata. Bahkan, hampir setengah dari total seller
    berasal dari state "SP". Dan setengah dari state yang ada memiliki total seller yang sangat jauh dibandingkan
    dengan 10 state terbanyak. Sehingga, perusahaan perlu mencari suatu mencari solusi atas permasalahan ini.""")


with st.container():
  st.write("---")

  st.subheader("Best Customer Based on RFM Parameters")
  
  fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(45, 10))
  colors = ["#1F9ED1"]
  
  sns.barplot(x="recency", y="customer_name", data=rfm_df.sort_values(by="recency", ascending=True).head(10), palette=colors, ax=ax[0], orient='h')
  ax[0].set_ylabel(None)
  ax[0].set_xlabel(None)
  ax[0].set_title("By Recency (days)", loc="center", fontsize=40)
  ax[0].tick_params(axis='y', labelsize=15)
  ax[0].tick_params(axis='x', labelsize=20)
  
  sns.barplot(x="frequency", y="customer_name", data=rfm_df.sort_values(by="frequency", ascending=False).head(10), palette=colors, ax=ax[1])
  ax[1].set_ylabel(None)
  ax[1].set_xlabel(None)
  ax[1].set_title("By Frequency", loc="center", fontsize=40)
  ax[1].tick_params(axis='y', labelsize=15)
  ax[1].tick_params(axis='x', labelsize=20)
  
  sns.barplot(x="monetary", y="customer_name", data=rfm_df.sort_values(by="monetary", ascending=False).head(10), palette=colors, ax=ax[2])
  ax[2].set_ylabel(None)
  ax[2].set_xlabel(None)
  ax[2].set_title("By Monetary", loc="center", fontsize=40)
  ax[2].tick_params(axis='y', labelsize=15)
  ax[2].tick_params(axis='x', labelsize=20)
  
  st.pyplot(fig)

  with st.expander("Kapan terakhir customer melakukan transaksi?"):
    st.write("Customer ke-29064 merupakan customer yang paling terakhir melakukan transaksi.")
  
  with st.expander("Seberapa sering seorang customer melakukan pembelian?"):
    st.write("Setelah dilakukan analisis dan visualisasi, rupaya setiap customer hanya melakukan satu kali pembelian. Oleh karena itu, perusahaan harus menganalisis lebih lanjut mengapa hal tersebut dapat terjadi.")

  with st.expander("Berapa banyak uang yang dihabiskan customer?"):
    st.write("Customer ke-8476 merupakan customer yang paling banyak mengeluarkan uang yaitu hampir sebesar 14000.")

st.caption('Copyright (C) ABDUL RAHMAN WAHID DATA SCIENCE LEARNING PATH IDCAMP2023')
