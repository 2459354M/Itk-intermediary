# standard
import streamlit as st
from core.ThemePage import Page
import core.MultiApp as hub

# custom

#####################
# main part
#####################


class Page2(Page):
    def __init__(self):
        super().__init__("Dictionary Keys",
                         "Dictionary Keys", ['nothing to report'])

    def main(self):
        pageDict = super().main()
        if hub.App.get_data():
            data = hub.App.get_data()
            st.write(data[0].keys())
