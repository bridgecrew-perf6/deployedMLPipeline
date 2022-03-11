import streamlit as st

from src.pages import PAGE_MAP


def main():
    st.sidebar.title("ML Pipeline")

    current_page = st.sidebar.radio("Go to", list(PAGE_MAP))
    PAGE_MAP[current_page]().app()


if __name__ == "__main__":
    main()