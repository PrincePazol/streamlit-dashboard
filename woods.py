# Import neccessary libraries and packages📦
import streamlit as st
import pandas as pd
import os
import warnings

# Filter out warnings⚠️
warnings.filterwarnings('ignore')

# Instantiate the app properties⚙️
st.set_page_config(page_title='Superstore Dashboard',
                   page_icon='📊',
                   layout='wide'
                  )

# Set the app title🖊️
st.title('🗺️ Superstore Dashboard')

# Adjust the title to top margin ⚙️
div = """<style>div.block-container{padding-top: 1rem;}</style>"""
st.markdown(div, unsafe_allow_html=True)

# Adding file uploader widget 📂
fl = st.file_uploader('Upload a file 📂',
                      ['csv', 'xlsx', 'xls']
                    )

# Capture the uploaded file into a variable 📦
if fl is not None:
  filename = fl.name
  df = pd.read_csv(filename, encoding='utf-8')
  st.write(f'{filename}')
  
else:
  path = r"C:\Users\princ\OneDrive\Desktop\streamLit\Data"
  os.chdir(path)
  df = pd.read_csv('Superstore.csv', encoding='utf-8')
  
# Extract the start and last order date
# from DataFrame 📃
date = 'Order Date'

# Convert the order date column to datetime dtype 🗓️
df[date] = pd.to_datetime(df[date])

# The earliest date of the order date column 🌱
start_date = pd.to_datetime(df[date]).min()
end_date = pd.to_datetime(df[date]).max()

# Create two columns for the two calendars 🗓️
col1, col2 = st.columns(2)

# Adding date components for filtering 🗓️
with col1:
 date_1 = pd.to_datetime(st.date_input('Start Date 🗓️: ', start_date))
  
with col2:
  date_2 = pd.to_datetime(st.date_input('End Date 🗓️: ', end_date))
  
# Add a sidebar to the app 🪟
region = st.sidebar.multiselect('Choose your Region',
                       df['Region'].unique())

# Filter the DataFrame based on selected dates 🔍
df = df[(df[date] >= date_1) & (df[date] <= date_2)].copy()

# # Temporary Display the DataFrame 📃
# st.dataframe(df, hide_index=True)

# Filter the DataFrame based on selected region 🔍
if not region:
  df2 = df.copy()
else:
  df2 = df[df['Region'].isin(region)]
  
# Filter the DataFrame based on selected state 🔍
state = st.sidebar.multiselect('Choose your State', df2['State'].unique())

if not state:
  df3 = df2.copy()
else:
  df3 = df2[df2['State'].isin(state)]

# Temporary Display the DataFrame 📃
st.dataframe(df3, hide_index=True)
