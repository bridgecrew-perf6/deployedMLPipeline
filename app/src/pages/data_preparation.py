import streamlit as st
from ..utils import Page

class Data_preparation(Page):
    def app(self):
        st.title("Data Preparation")
        st.write(st.session_state)