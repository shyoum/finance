import streamlit as st
import stock_check
import stock_update
import news_crawling
import sentiment_analysis
import final_selection

def main():
    st.sidebar.title("메뉴")
    option = st.sidebar.selectbox("선택", [
        "Check",
        "Update",
        "News",
        "Sentiment",
        "Select"
    ])

    if option == "Check":
        stock_check.run()
    elif option == "Update":
        stock_update.run()
    elif option == "News":
        news_crawling.run()
    elif option == "Sentiment":
        sentiment_analysis.run()
    elif option == "Select":
        final_selection.run()

if __name__ == "__main__":
    main()
