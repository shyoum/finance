import streamlit as st
import FinanceDataReader as fdr

def run():
    st.title("미국 주식 전 종목 데이터 업데이트")

    # 1. 미국 주식 전체 종목 코드 리스트 조회
    us_stock_list = fdr.StockListing('NASDAQ')  # NASDAQ 전체 종목
    # 또는 NYSE, AMEX 등 다른 거래소 추가 가능

    st.write(f"총 {len(us_stock_list)}개 미국 주식 종목을 업데이트합니다.")

    if st.button("업데이트 시작"):
        # 예: 각각 종목의 최근 데이터 조회 코드(간단히 예시)
        for symbol in us_stock_list['Symbol'][:10]:  # 시연용 10개 종목만 처리
            st.write(f"업데이트 중: {symbol}")
            df = fdr.DataReader(symbol, exchange='NASDAQ')
            # 여기서 df를 DB 저장 또는 파일 저장 등 원하는 처리 추가
            
        st.success("업데이트 완료")
