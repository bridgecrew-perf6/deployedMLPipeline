import streamlit as st
from ..utils import Page, text_area

default_labels = {
    'objective': "What are the business objectives of this Project?",
    'situation': "What is the current situation? Provide current KPI values if possible.",
    'success': "What are the success criteria for the project? What is the expected effect of the project?",
    'assumptions': "What assumptions are we making? How do we confirm/contradict them?"
}
default_answers = {
    'objective': "Example: \nOptimize Marketing Channel Allocation",
    'situation': "Example: \nIn the last 12 months, we allocated 90% of our marketing budget on online platforms. \
                    \nHowever, in the past 3 months, there is a 40% reduction in website visits which we attribute to \
                    \nthe easing out of covid restrictions.",
    'success': "Example: \nImprovement in website visits within the testing period of 2 weeks.",
    'assumptions': "Example:\n1. Change in website visits is driven by change in covid restrictions.\
                    \n2. Testing period of 2 weeks is suffient to determine results."
}

class Business_understanding(Page):
    def app(self):
        st.title("Business Understanding")
        
        st.header("Objectives")
        text_area(default_labels, default_answers, "objective")
        
        st.header("Current Situation")
        text_area(default_labels, default_answers, "situation")

        st.header("Success Criteria")
        text_area(default_labels, default_answers, "success")

        st.header("Assumptions")
        text_area(default_labels, default_answers, "assumptions")

        if st.button(label="Save Answers"):
            pass