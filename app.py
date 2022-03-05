import yfinance as yf
import streamlit as st
import pandas as pd
import datetime as dt

if __name__ == '__main__':
    st.write("""

    # Simple Stock Price App

    Resource: https://www.youtube.com/watch?v=JwSS70SZdyM

    What I did as an **extension**: Added a filter to change the date range for our line charts!

    Shown are the stock **closing** price and ***volume*** of Google!

    """)

    # Define ticker symbol
    tickerSymbol = 'GOOGL'

    # get data on ticker
    def fetch_data():
        tickerData = yf.Ticker(tickerSymbol)
        return tickerData

    tickerData = fetch_data()

    start_date = '2010-5-31'
    end_date = '2022-2-28'

    # get historical prices for ticker
    tickerDf = pd.DataFrame(tickerData.history(period = '1d', start = start_date, end = end_date))

    tickerDf['Date'] = pd.to_datetime(tickerDf.index).date

    st.title("Ticker Data")
    st.dataframe(tickerDf)

    st.title("Date Range")
    min_date = dt.datetime.strptime(start_date, '%Y-%m-%d')
    max_date = dt.datetime.strptime(end_date, '%Y-%m-%d')

    start = st.date_input("Pick a date:", min_value = min_date, max_value = max_date, value = min_date)
    end = st.date_input("Pick a date:", min_value = min_date, max_value = max_date, value = max_date)

    "Start date selected: ", start
    "End date selected: ", end

    new_copy = tickerDf.loc[(tickerDf.Date >= start) & (tickerDf.Date <= end),:]

    st.title(("Closing Price - " + tickerSymbol))
    st.line_chart(new_copy.loc[:,'Close'])

    st.title("Closing Price - " + tickerSymbol)
    st.line_chart(new_copy.loc[:,'Volume'])
