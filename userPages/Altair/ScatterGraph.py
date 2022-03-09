# standard
import streamlit as st
from core.ThemePage import Page
import core.MultiApp as hub
import plotly.express as px
# custom

#####################
# main part
#####################


class Page2(Page):
    def __init__(self):
        super().__init__("Scatter Graph",
                         "Scatter Graph", ['nothing to report'])

    def main(self):
        pageDict = super().main()
