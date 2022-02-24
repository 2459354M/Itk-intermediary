# standard
import streamlit as st
from core.ThemePage import Page
import core.MultiApp as hub
# custom
import pandas as pd
import json


#####################
# main part
#####################

class Page1(Page):
    def __init__(self):
        super().__init__("Json Display", "Json_Display", ['nothing to report'])

    def main(self):
        pageDict = super().main()
        if(hub.App.get_data()):
            data = hub.App.get_data()
            index = st.slider("Select Index to Display",
                              min_value=0, max_value=len(data) - 1, value=0)
            st.json(data[index])
