import streamlit as st
import plotly.express as px
import pandas as pd
import os
import warnings
warnings.filterwarnings('ignore')

# Page configuration
st.set_page_config(
    page_title='편의점 매출 예측',
    page_icon='🌷',
    layout='wide',
    initial_sidebar_state='expanded'
)

# title of app
# st.subheader('🌷 편의점 매출 예측 시각화 연습')

# load dataset
df = pd.read_csv('./project_data/비골목_streamlit.csv')
# st.caption('원본 데이터프레임')
# st.write(df.head())

# input widgets
st.sidebar.header('🌷 편의점 매출 예측 시각화 연습')
st.sidebar.write('---')
st.sidebar.subheader('비골목상권 : 기준을 선택하세요')
year = st.sidebar.selectbox('연도',
                     df['기준_년_코드'].unique())
quarter = st.sidebar.selectbox('분기', df['분기'].unique())
place_code = st.sidebar.selectbox('상권코드',
                             df['상권_코드'].unique())

place_name = df[df['상권_코드'] == place_code]['상권_코드_명'].iloc[0]
st.sidebar.caption(f'--->> 선택하신 상권은 {place_name}입니다.')

# 시각화용 데이터 필터링
filtered_df = df[(df['기준_년_코드'] == year) & (df['상권_코드'] == place_code) & (df['분기'] == quarter)]

# Plotly 그래프
st.subheader(f'{year}년 {place_name} {quarter}분기')
st.write(filtered_df)
st.write('---')

st.markdown('#### 상권 현황')
col1, col2, col3 = st.columns(3)
with col1:
    st.metric('총 상주인구', filtered_df['총 상주인구 수'].iloc[0])
with col2:
    st.metric('총 직장인구', filtered_df['총_직장인구_수'].iloc[0])
with col3:
    st.metric('편의점 점포수', filtered_df['점포수'].iloc[0])

# 시간대별 매출
st.write('---')
max_sales = filtered_df['매출'].max()
max_sales_time = filtered_df[filtered_df['매출'] == max_sales]['시간대'].reset_index(drop=True)
st.markdown(f'#### 👉 {max_sales_time.iloc[0]}번 시간대 매출이 가장 높습니다!')

fig = px.bar(
        filtered_df,
        x='시간대',
        y='매출',
        labels={'시간대': '시간대', '매출': '매출액'},
        title=f'💰 시간대별 매출액'
    )
# 매출액이 가장 높은 시간대 데이터 포인트의 색상 변경 (예: 빨간색)
fig.update_traces(marker_color='pink')
st.plotly_chart(fig, use_container_width=True)

# 시간대별 생활인구수
fig = px.bar(
        filtered_df,
        x='시간대',
        y='시간대_생활인구_수',
        labels={'시간대': '시간대', '시간대_생활인구_수': '시간대별 생활인구'},
        title=f'🏚️ 시간대별 생활인구 수'
    )
st.plotly_chart(fig, use_container_width=True)



st.write('---')
st.markdown('#### 대중교통 현황')
col1, col2 = st.columns(2)
with col1:
    fig = px.bar(
        filtered_df,
        x='시간대',
        y='시간대_버스_승하차승객수',
        labels={'시간대': '시간대', '시간대_버스_승하차승객수': '버스 승객수'},
        title=f'🚌 시간대 별 버스 승하차 승객수'
    )
    st.plotly_chart(fig, use_container_width=True)


with col2:
    fig = px.bar(
        filtered_df,
        x='시간대',
        y='시간대_지하철_승하차승객수',
        labels={'시간대': '시간대', '시간대_지하철_승하차승객수': '지하철 승객수'},
        title=f'🚊 시간대 별 지하철 승하차 승객수'
    )
    st.plotly_chart(fig, use_container_width=True)