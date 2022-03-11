import streamlit as st

from src.pages import PAGE_MAP
import pandas as pd

# st.title("Heart Disease Prediction")

# # Side Bar
# st.sidebar.title("Data Science Pipeline")

# st.sidebar.radio("Go to", 
# ['Business Understanding',
#  'Data Understanding', 
#  'Data Preparation', 
#  'Modeling', 
#  'Evaluation', 
#  'Deployment'])

# df = pd.DataFrame({
#   'first column': [1, 2, 3, 4],
#   'second column': [10, 20, 30, 40]
# })

def main():
    st.sidebar.title("ML Pipeline")

    current_page = st.sidebar.radio("Go to", list(PAGE_MAP))
    PAGE_MAP[current_page]().app()

if __name__ == "__main__":
    main()