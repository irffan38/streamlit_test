import streamlit as st 
import requests

st.markdown("<div style='text-align: center;'><img src='https://www.google.com/url?sa=i&url=https%3A%2F%2Ffavpng.com%2Fpng_view%2Fyoutube-humour-funny-face-youtube-joke-laughter-png%2FpgTYSZU9&psig=AOvVaw2LVVdNtrPHAyetdEauj7I_&ust=1748590997626000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCKCE9ZyXyI0DFQAAAAAdAAAAABAE' width='150'></div>", unsafe_allow_html=True)

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

if response.status_code == 200:
    data = response.json()
    st.write(f'Exchange Rates (Base: {base_currency}):')
    st.json(data)  # Display JSON formatted response
else:
    st.error(f"API call failed with status code: {response.status_code}")

