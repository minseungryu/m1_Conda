import streamlit as st
import plotly.express as px
import pandas as pd
import os
import warnings
warnings.filterwarnings('ignore')

# 페이지 자체 이름
st.set_page_config(page_title="편의점 매출분석", page_icon=":convenience_store:", layout="wide")

# 페이지 타이틀
st.title(" :bar_chart: 편의점 매출분석 대시보드")
# st.markdown('<style>div.block-container{padding-top:1rem}</style>', unsafe_allow_html=True)

# 데이터 로드하는 파트 만들기
f1 = st.file_uploader(":file_folder:  Upload a File", type=(['csv', 'txt', 'xlsx', 'xls']))
if f1 is not None:
    filename = f1.name
    st.write(filename)
    df = pd.read_csv(filename, encoding="ISO-8859-1")
else:
    os.chdir(r"/Users/angela/m1_streamlit")
    df = pd.read_csv('Sample - Superstore.csv', encoding="ISO-8859-1")

# 컬럼 2개 생성
col1, col2 = st.columns((2))
df['Order Date'] = pd.to_datetime(df['Order Date'])

# 최대, 최소 날짜 지정가능
startDate = pd.to_datetime(df['Order Date']).min()
endDate = pd.to_datetime(df['Order Date']).max()

with col1 :
    date1 = pd.to_datetime(st.date_input("Start Date", startDate))

with col2 :
    date2 = pd.to_datetime(st.date_input("End Date", endDate))

df = df[(df['Order Date'] >= date1) & (df['Order Date'] <= date2)].copy()

# 사이드바
st.sidebar.header("Choose your filter: ")

# 지역 선택
region = st.sidebar.multiselect("Pick your Region", df['Region'].unique())
if not region:
    df2 = df.copy()
else:
    df2 = df[df["Region"].isin(region)]

# 주 선택
state = st.sidebar.multiselect("Pick your State", df2['State'].unique())
if not state:
    df3 = df2.copy()
else:
    df3 = df2[df2['State'].isin(state)]

# 도시 선택
city = st.sidebar.multiselect("Pick the City", df3['City'].unique())

# 데이터 필터(지역,주, 도시 기준)
if not region and not state and not city:
    filtered_df = df
elif not state and not city:
    filtered_df = df[df['Region'].isin(region)]
elif not region and not city:
    filtered_df = df[df['State'].isin(state)]
elif state and city:
    filtered_df = df3[df['State'].isin(state) & df3['City'].isin(city)]
elif region and city:
    filtered_df = df3[df['Region'].isin(region) & df3['City'].isin(city)]
elif region and state:
    filtered_df = df3[df['Region'].isin(region) & df3['City'].isin(state)]
elif city:
    filtered_df = df3[df3['City'].isin(city)]
else:
    filtered_df = df3[df3['Region'].isin(region) & df3['State'].isin(state) & df3['City'].isin(city)]

category_df = filtered_df.groupby(by = ['Category'], as_index = False)['Sales'].sum()

with col1:
    st.subheader("category with Sales")
    fig = px.bar(category_df, x = "Category", y = "Sales", text = ['${:,.2f}'.format(x) for x in category_df['Sales']], template= "seaborn")
    st.plotly_chart(fig, use_container_width=True, height = 200)

with col2:
    st.subheader("Region with Sales")
    fig = px.pie(filtered_df, values= "Sales", names = "Region", hole= 0.5)
    fig.update_traces(text = filtered_df['Region'], textposition = 'outside')
    st.plotly_chart(fig, use_container_width=True)

