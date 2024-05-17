import pandas as pd
import streamlit as st
import re
 
def validate_description(description):
    pattern = r'^[ASR]/[A-Z]{2}/[A-Z]{4}/'
    return bool(re.match(pattern, description))
 
def process_file(file):
    df = pd.read_excel(file)
    
    df['Valid Description'] = df['Notification Description'].apply(lambda x: 'Yes' if validate_description(str(x)) else 'No')
    df['Invalid Description'] = df['Notification Description'].apply(lambda x: 'Yes' if not validate_description(str(x)) else 'No')
    
    return df
 
def main():
    st.title('Naming Convention Validator')
    
    uploaded_file = st.sidebar.file_uploader('Choose an Excel file', type=['xlsx', 'xls'])
    
    if uploaded_file is not None:
        df = process_file(uploaded_file)
        st.write(df)
        
        csv = df.to_csv(index=False)
        st.download_button(
            label='Download CSV',
            data=csv,
            file_name='validated_data.csv',
            mime='text/csv'
        )
 
if __name__ == '__main__':
    main()
