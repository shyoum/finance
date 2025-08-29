import streamlit as st
import FinanceDataReader as fdr
import datetime
from requests.exceptions import HTTPError

st.title('주가 데이터 조회')

ticker = st.text_input('티커를 입력하세요 (예: 005930, AAPL 등)', '')

if ticker:
    end_date = datetime.date.today()
    start_date = end_date - datetime.timedelta(days=30)

    try:
        df = fdr.DataReader(ticker, start_date, end_date)
        if not df.empty:
            recent_7_business_days = df.tail(7)
            st.subheader(f'{ticker} 최근 7영업일 데이터')
            st.dataframe(recent_7_business_days)
        else:
            st.warning('데이터가 없습니다. 티커를 확인하세요.')
    except HTTPError:
        st.error('잘못된 티커입니다. 다시 입력해주세요. (국장은 종목코드, 미장은 티커로 입력)')
    except Exception as e:
        st.error(f'오류가 발생했습니다: {e}')
