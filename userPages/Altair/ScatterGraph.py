# standard
import streamlit as st
from core.ThemePage import Page
import core.MultiApp as hub
# custom
import altair as alt
import pandas as pd
from strlittemplate.util import Flattenjson, Value
#####################
# main part
#####################


class Page2(Page):
    def __init__(self):
        super().__init__("Scatter Graph",
                         "Scatter Graph", ['nothing to report'])

    def main(self):
        pageDict = super().main()
        data = hub.App.get_data()
        if data:
            # only keys which exist in all instances
            flatdatakeys = Flattenjson.flattenjson(data)
            if flatdatakeys is False:
                raise ValueError("Cannot interpret data")

            stringkeys = list(flatdatakeys.keys())
            stringkeys.insert(0, "none")

            index1 = st.selectbox("Select a component:", stringkeys, index=0)

            value1, value2 = [], []
            if index1 != "none":
                for i in data:
                    value1.append(Value.getValue(
                        i, flatdatakeys, index1))
                value1 = Value.count(value1)
                x, y = [], []
                for key, value in value1.items():
                    x.append(key)
                    y.append(value)

                source = pd.DataFrame({index1: x, 'count': y})
                try:
                    chart = alt.Chart(source.reset_index()).mark_circle(
                        size=60).encode(
                        x='index',
                        y='count',
                        color=index1
                    ).interactive()

                    rule = alt.Chart(value1).mark_rule(color='red').encode(
                        y='mean(count):Q'
                    )

                    st.altair_chart(chart.properties(
                        width=600,
                        height=500))
                except BaseException:
                    st.write("Cannot generate scatter graph")
