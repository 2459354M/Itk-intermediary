# standard
import streamlit as st
from core.ThemePage import Page
import core.MultiApp as hub
import datetime as dt
# custom

#####################
# main part
#####################


class Page1(Page):
    def __init__(self):
        super().__init__("Date", "Date", ['nothing to report'])

    def main(self):
        pageDict = super().main()
        st.write("Basic Date Grab Example")
        if hub.App.get_data():
            data = hub.App.get_data()
            st.write(data[0]["stateTs"])
            mydate = hub.App.parse_date(data[0]["stateTs"])
            st.write(mydate)
