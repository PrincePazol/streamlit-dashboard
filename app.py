# Import streamlit and python libraries
import streamlit as st
import pandas as pd
import numpy as np

# # Start a simple streamlist app
# st.write("hello world of streamlit")

# # Create a dataframe to display on screen
# df = pd.DataFrame({
#   'name': ['prince', 'osei', 'bonsu', 'pazol'],
#   'city': ['atlanta', 'accra', 'techiman', 'london'],
#   'age': [20, 30, 40, 50],
#   'networth': [2000000, 5000000, 10000000, 5000000]
# })

# df

# Create a dataframe to store 
dataframe = pd.DataFrame(
  np.random.randn(10, 20),
  columns = ('col %d' % i for i in range(20))
)

# Create a streamlit table
st.table(dataframe)

# Create a chart data
chart_data = pd.DataFrame(
  np.random.randn(20, 3),
  columns=['a', 'b', 'c']
)

# Create a line chart
st.line_chart(chart_data)

# Create a map
map_data = pd.DataFrame(
  np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
  columns=['lat', 'lon']
)

st.map(map_data)

# This is a widget
x = st.slider('x')
st.write(f"{x} is square of {x * x}")

# You can access the value at point with:
st.text_input("Your name", key="name")

st.session_state.name