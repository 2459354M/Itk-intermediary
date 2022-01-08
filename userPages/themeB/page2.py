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
        super().__init__("Chart Demo",
                         "Basic Pie Chart Example", ['nothing to report'])

    def main(self):
        pageDict = super().main()

        data = hub.App.get_data()

        index = st.slider("Select point at which to disregard institution",
                          min_value=0, max_value=10, value=5)

        inst_number = {}
        for i in data:
            if i["institution"]["name"] in inst_number.keys():
                inst_number[i["institution"]["name"]] += 1
            else:
                inst_number[i["institution"]["name"]] = 1

        titles = [i for i in inst_number.keys()]
        if(index > 1):
            inst_number["other"] = 0
        for i in titles:
            if(inst_number[i] < index):
                inst_number["other"] += inst_number[i]
                inst_number.pop(i)
        print(inst_number)

        values = []
        for i in inst_number.keys():
            values.append(inst_number[i])

        chart = px.pie(values=values, names=inst_number.keys())
        st.plotly_chart(chart)
