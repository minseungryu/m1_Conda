# -*- coding:utf-8 -*-
import streamlit as st
import os
import joblib
import warnings
warnings.filterwarnings('ignore')
from ml_app import run_ml_app

def main():
    menu = ["Home", "시각화", "머신러닝"]
    choice = st.sidebar.selectbox("메뉴", menu)

    if choice == "Home":
        st.subheader("Home")
    elif choice == "시각화":
        st.subheader("자료 시각화")
        # run_eda_app()
    elif choice == "머신러닝":
        st.subheader("머신러닝")
        run_ml_app()
    else:
        pass

if __name__ == "__main__":
    main()