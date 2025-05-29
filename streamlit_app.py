import streamlit as st 
import requests

# Show UMPSA logo
st.image("https://upload.wikimedia.org/wikipedia/ms/2/29/Logo_Universiti_Malaysia_Pahang.svg", width=200)

# Set the app title 
st.title('Ipan Exchancer') 

# Add a welcome message 
st.write('No money, No talk') 

# Create a text input 
widgetuser_input = st.text_input('Enter a custom message:', 'Hello, Streamlit!') 

# Display the customized message 
st.write('Customized Message:', widgetuser_input)

# Dropdown to select base currency
currencies = ['MYR', 'USD', 'EUR', 'GBP', 'SGD', 'JPY', 'CNY', 'AUD', 'CAD']
base_currency = st.selectbox('Select base currency:', currencies)

# Fetch exchange rates using selected base currency
url = f'https://api.vatcomply.com/rates?base={base_currency}'
response = requests.get(url)

if response.status_cod_
