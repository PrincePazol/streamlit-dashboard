# Import the neccessary libraries for the project
import streamlit as st
import pandas as pd
import numpy as np

# Add a customized header to the app
st.title(':rainbow[*Lightweight EDA Web App*]')

# Add a title to the web App
st.header('Uber pickups in NYC❤️')

# Create a date column variable
DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz')

# Effortless caching
@st.cache_data

# A function to load the data from s3 
def load_data(nrows):
  """This function loads data from the source
     and rename the column names, and finally
     convert the date/time column to an actual
     DateTime data type.
  """
  data = pd.read_csv(DATA_URL, nrows=nrows)
  lowercase = lambda x: str(x).lower()
  data.rename(lowercase, axis='columns', inplace=True)
  data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])

  return data

# Create a text element and let the reader know
# the data is loading
data_load_state = st.text('Loading data...')

# Load 10,000 rows of data into the dataframe
data = load_data(10000)

# Notify the reader that the data was successfully loaded
data_load_state.text('Done! (using st.cache_data)')

# # Inspect the raw data
# st.subheader(':rainbow[Raw data]', divider='rainbow')
# st.write(data)
if st.checkbox('Show raw data'):
  st.subheader('Raw data')
  st.write(data)

# Subheader for histogram
st.subheader('Number of pickups by hour')

hist_values = np.histogram(
  data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]

st.bar_chart(hist_values)

# Time slider for filtering the DataFrame
time_selected = st.slider('Choose time range 🕰️', 0, 24, 17)
data_slider = data[data[DATE_COLUMN].dt.hour.eq(time_selected)]

# Display the filtered dataframe
data_slider

# Visualize the dataset on a map
st.subheader(f'Map of all pickups in NYC❤️ at {time_selected}:00')
st.map(data_slider)