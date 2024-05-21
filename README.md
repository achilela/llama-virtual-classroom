## Naming Convention Validator
 
This project aims to validate naming conventions in a given Excel file and prepare the data for creating a naming notification spam classifier. The goal is to use this validated data to fine-tune a large language model (LLM) such as Phi-3 or Llama3 for spam classification purposes.
 
## Features
 
- Upload an Excel file containing a "Notification Description" column
- Validate the naming convention in the "Notification Description" column
- The naming convention pattern follows:
  - Start with a single character from the set {A, S, R}
  - Followed by a forward slash
  - Followed by exactly two uppercase letters
  - Followed by a forward slash
  - Followed by either:
    - Exactly four uppercase letters, or
    - Exactly three uppercase letters followed by a single digit from 1 to 4
  - Ending with a forward slash
- Add "Valid Description == Yes" and "Invalid Description == No" columns to indicate whether each entry follows the naming convention as per Unisup procedure
- Display the processed data in a Streamlit web app
- Download the processed data as a CSV file
 
## Usage
 
1. Install the required dependencies:
   ```
   pip install pandas streamlit
   ``` 
2. Run the Streamlit app:
   ```
   streamlit run app.py
   ```
3. Upload an Excel file containing a "Notification Description" column using the sidebar file uploader.
 
4. The app will validate the naming convention in the "Notification Description" column and display the processed data.
 
5. Click the "Download CSV" button to download the processed data as a CSV file.
 
## Future Work
 
The validated data obtained from this project will be used to fine-tune a large language model (LLM) such as Phi-3 or Llama3. The fine-tuned model will be used to build a naming notification spam classifier, which can help identify and filter out spam notifications based on their naming patterns.
 
By leveraging the power of LLMs and the validated naming convention data, my goal is to create an accurate and efficient naming spam classifier for notifications.
