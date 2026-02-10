import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load processed data
df = pd.read_csv("csv_files/processed_trader_sentiment_data.csv")

st.set_page_config(page_title="Trader Behavior Dashboard", layout="wide")

st.title("📊 Trader Behavior vs Market Sentiment")

# Sidebar filter
sentiment_filter = st.sidebar.selectbox(
    "Select Market Sentiment",
    ["All", "Fear", "Greed"]
)

if sentiment_filter != "All":
    df = df[df["sentiment"] == sentiment_filter]

st.subheader("PnL Distribution")
fig, ax = plt.subplots()
sns.boxplot(data=df, x="sentiment", y="Closed PnL", ax=ax)
st.pyplot(fig)

st.subheader("Trade Size Distribution")
fig, ax = plt.subplots()
sns.boxplot(data=df, x="sentiment", y="abs_size_usd", ax=ax)
st.pyplot(fig)

st.subheader("Win Rate by Sentiment")
win_rate = df.groupby("sentiment")["is_profitable"].mean()
fig, ax = plt.subplots()
win_rate.plot(kind="bar", ax=ax)
st.pyplot(fig)

st.subheader("Trade Count by Sentiment")
trade_count = df["sentiment"].value_counts()
fig, ax = plt.subplots()
trade_count.plot(kind="bar", ax=ax)
st.pyplot(fig)
