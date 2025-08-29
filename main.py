import streamlit as st
import stock_check
import news_sentiment

def main():
    st.sidebar.title("메뉴")
    option = st.sidebar.selectbox("기능 선택", ["주가 데이터 획득 및 후보 추출", "뉴스 크롤링 및 감성 분석"])

    if option == "주가 데이터 획득 및 후보 추출":
        stock_check.run()
    elif option == "뉴스 크롤링 및 감성 분석":
        news_sentiment.run()

if __name__ == "__main__":
    main()
