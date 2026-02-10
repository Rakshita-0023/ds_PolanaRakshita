# Trader Behaviour vs Market Sentiment Analysis

## Overview
This project analyses how trader behaviour changes under different market sentiment regimes—Fear and Greed—using historical trading data and the Bitcoin Fear & Greed Index. The goal is to identify behavioural patterns related to risk-taking, trading activity, and profitability that can inform sentiment-aware trading strategies.

## Google Colab Notebook
Main analysis notebook (view-only):
https://colab.research.google.com/drive/1Rqz4jMUB2SQiAhNk6A0U6EXrIlBnsmQO?usp=sharing

## How to Run

1. Open the Google Colab notebook:
   https://colab.research.google.com/drive/1Rqz4jMUB2SQiAhNk6A0U6EXrIlBnsmQO?usp=sharing
2. Run all cells sequentially to reproduce the analysis and outputs.
3. All generated charts are saved in the `outputs/` directory.


## Datasets
1. **Bitcoin Fear & Greed Index**
   - Provides daily market sentiment labels.
   - Sentiment is simplified into two regimes: Fear and Greed.

2. **Historical Trader Data (Hyperliquid)**
   - Trade-level data including trade size, position direction, timestamps, and closed PnL.

## Methodology
- Cleaned and standardised both datasets.
- Aligned timestamps at the daily level.
- Merged trader data with sentiment labels by date.
- Engineered key features:
  - Risk exposure (proxied by absolute trade size in USD)
  - Profitability (closed PnL and win rate)
- Performed Exploratory Data Analysis (EDA) to compare behavior across Fear and Greed regimes.
- Conducted trader segmentation based on activity level and risk exposure.

## Key Insights
- Trading activity and risk-taking increase during Greed regimes.
- PnL volatility is significantly higher during Fear regimes.
- Risk exposure remains elevated during Fear, suggesting panic-driven or recovery-based trading.
- Frequent traders exhibit distinct performance characteristics compared to infrequent traders.

## Project Structure
ds_PolanaRakshita/ ├── notebook_1.ipynb # Main analysis notebook (Google Colab) ├── csv_files/ # Processed and intermediate CSV files ├── outputs/ # Visualizations and charts ├── ds_report.pdf # Final summarised report (1 page) ├── app.py # Optional Streamlit dashboard └── README.md # Project documentation

## How to Run
1. Open `notebook_1.ipynb` in Google Colab.
2. Run cells sequentially to reproduce the analysis and outputs.
3. (Optional) To run the dashboard locally:
   ```bash
   streamlit run app.py

Optional Dashboard
An optional Streamlit dashboard (app.py) is included for interactive exploration of trader behavior across Fear and Greed sentiment regimes.
Author
Rakshita Polana
