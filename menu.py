import streamlit as st

def select_menu():
    st.sidebar.title("메뉴")
    option = st.sidebar.selectbox("선택", [
        "Check",
        "Update",
        "News",
        "Sentiment",
        "Select"
    ])
    return option
