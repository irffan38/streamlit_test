import streamlit as st 
import requests

# Show UMPSA logo
st.image("https://upload.wikimedia.org/wikipedia/en/thumb/0/01/UMPSA_LOGO_2023.svg/512px-UMPSA_LOGO_2023.svg.png", width=200)

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

# ✅ FIXED: Corrected the typo here
if response.status_code == 200:
    data = response.json()
    st.write(f'Exchange Rates (Base: {base_currency}):')
    st.json(data)
else:
    st.error(f"API call failed with status code: {response.status_code}")
