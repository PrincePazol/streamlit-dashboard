# Import streamlit and python libraries
import streamlit as st
import pandas as pd

# Start a simple streamlist app
st.write("hello world of streamlit")

# Create a dataframe to display on screen
df = pd.DataFrame({
  'name': ['prince', 'osei', 'bonsu', 'pazol'],
  'city': ['atlanta', 'accra', 'techiman', 'london'],
  'age': [20, 30, 40, 50],
  'networth': [2000000, 5000000, 10000000, 5000000]
})

df