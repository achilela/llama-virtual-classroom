import streamlit as st
import pandas as pd
 
def validate_data(data):
    # Define the pattern
    pattern = r'^[A-Z]\/[A-Z]{2}\/[A-Z]{4}\/$'
 
    # Apply the pattern to the data
    data['valid'] = data['Notification Description'].str.contains(pattern)
 
    # Split the data into valid and invalid
    valid_data = data[data['valid']]
    invalid_data = data[~data['valid']]
 
    return valid_data, invalid_data
 
st.sidebar.header('Upload File')
uploaded_file = st.sidebar.file_uploader("Choose a file", type="xlsx")
 
if uploaded_file is not None:
    data = pd.read_excel(uploaded_file)
 
    # Validate the data
    valid_data, invalid_data = validate_data(data)
 
    st.header('Valid Data')
    st.write(valid_data)
 
    st.header('Invalid Data')
    st.write(invalid_data)
else:
    st.info('☝️ Upload a CSV file')
