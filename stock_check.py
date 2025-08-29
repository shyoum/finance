import streamlit as st
import FinanceDataReader as fdr
import datetime
from requests.exceptions import HTTPError

def run():
    st.title('주가 데이터 조회')
    ticker = st.text_input('티커를 입력하세요 (예: 005930, AAPL 등)').strip()

    if ticker:
        end_date = datetime.date.today()
        start_date = end_date - datetime.timedelta(days=30)

        try:
            df = fdr.DataReader(ticker, start_date, end_date)
            
            if df.empty:
                st.warning('데이터가 없습니다. 입력하신 티커를 다시 확인해 주세요.')
            else:
                recent_7_days = df.tail(7)
                st.subheader(f'{ticker.upper()} 최근 7영업일 주가 데이터')
                st.dataframe(recent_7_days)
        
        except HTTPError:
            st.error('잘못된 티커입니다. 종목코드를 확인하고 다시 입력해 주세요. (국내주는 종목코드, 미국주는 Ticker 명칭)')
        except Exception as e:
            st.error(f'알 수 없는 오류가 발생했습니다: {e}')
    else:
        st.info('조회할 티커를 입력해 주세요.')
