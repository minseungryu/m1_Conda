# -*- coding:utf-8 -*-
import streamlit as st
import joblib
import os
import numpy as np
import pandas as pd

def run_ml_app():
    st.caption('머신러닝 예측 페이지----')

    # data
    df = pd.read_csv('./project_data/Final_골목상권_데이터230917.csv')
    st.write(df.head())

    # model import
    model_file = "models/gm_model.pkl"
    model = joblib.load(open(os.path.join(model_file), 'rb'))
    st.write(model)

    # layout
    st.subheader('상권코드 선택!')
    market_code = st.selectbox('상권코드', df['상권_코드'].unique())

    feature_list = ['시간대1', '시간대2', '시간대3', '시간대4', '시간대5', '분기_1', '분기_2', '분기_3',
       '총 가구 수', '총_직장인구_수', '상권내_총_아파트_세대_수', '배후지_총_아파트_세대_수',
        '시간대_생활인구_수', '평일_생활인구_평균', '주말_생활인구_평균', '면적당_점포_수',
       '직장인구/상주인구', '면적당_집객시설_수']

    st.subheader('모델 결과를 확인해주세요!')


"""
    # layout
    col1, col2 = st.columns(2)
    with col1:
        st.subheader('피쳐별 수치 조절!')
        market_code = st.selectbox('상권코드', )
        # sepal_length = st.select_slider('Sepal Length', options = np.arange(1, 11))

        # sample_list = [sepal_length, sepal_width, petal_length, petal_width]
        # st.write(sample_list)
    
    with col2:
        st.subheader('모델 결과를 확인해주세요!')

        # 배열로 만듦
        one_sample = np.array(sample_list).reshape(1, -1)
        st.write(one_sample)
        st.write(one_sample.shape)

        # 범주 예측
        prediction = model.predict(one_sample)
        st.write(prediction)

        # 확률값 예측
        pred_prob = model.predict_proba(one_sample)
        st.write(pred_prob)

        if prediction == 0:
            st.success("Setosa 종")
            pred_proba_scores = {
                "1일 확률": pred_prob[0][0] * 100, 
                "0일 확률": pred_prob[0][1] * 100, 
            }
            st.write(pred_proba_scores)
            st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Irissetosa1.jpg/220px-Irissetosa1.jpg')
        elif prediction == 1:
            st.success("00 종")
            pred_proba_scores = {
                "1일 확률": pred_prob[0][0] * 100, 
                "0일 확률": pred_prob[0][1] * 100, 
            }
            st.write(pred_proba_scores)
            st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Blue_Flag%2C_Ottawa.jpg/220px-Blue_Flag%2C_Ottawa.jpg')
        else:
            st.warning("아이돈노!")
    """