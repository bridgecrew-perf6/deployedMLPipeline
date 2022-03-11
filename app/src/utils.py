import streamlit as st
from abc import ABC, abstractmethod


class Page(ABC):
    @abstractmethod
    def app(self):
        pass


def text_area(default_labels, default_answers, section):
    """Receives user text input and store it into Session State for reuse"""
    key = f'answer_{section}'
    answer = None
    if key not in st.session_state:
        answer = st.text_area(label=default_labels[section],
                              value=default_answers[section])
    else:
        answer = st.text_area(label=default_labels[section],
                              value=st.session_state[key])
    
    st.session_state[key] = answer


def add_custom_css():
    pass