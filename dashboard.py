import streamlit as st
import plotly.express as px
import pandas as pd
import os
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title='Superstore!!!', page_icon=':bar_chart', layout='wide')

st.title(' :bar_chart: Sample Superstore EDA')
st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)

fl = st.file_uploader('📂 Upload a file', type=(['csv', 'txt', 'xlsx', 'xls']))

if fl is not None:
  filename = fl.name
  st.write(filename)
  df = pd.read_csv(filename, encoding='ISO-8859-1')
else:
  os.chdir(r"C:\Users\princ\Desktop\Streamlit\Data")
  df = pd.read_csv('Superstore.csv', encoding='ISO-8859-1')
  

col1, col2 = st.columns(2)
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Getting the min and max date
start_date = pd.to_datetime(df['Order Date']).min()
end_date = pd.to_datetime(df['Order Date']).max()

with col1:
  date_1 = pd.to_datetime(st.date_input('Start Date', start_date))

with col2:
  date_2 = pd.to_datetime(st.date_input('End Date', end_date))
  
df = df[(df['Order Date'] >= date_1) & (df['Order Date'] <= date_2)].copy()

st.sidebar.header('Choose your filter: ')
# Create for region
region = st.sidebar.multiselect('Pick your Region', df['Region'].unique())

if not region:
  df2 = df.copy()
else:
  df2 = df[df['Region'].isin(region)]
  
# Create for state
state = st.sidebar.multiselect('Pick your State', df2['State'].unique())

if not state:
  df3 = df2.copy()
else:
  df3 = df2[df2['State'].isin(state)]