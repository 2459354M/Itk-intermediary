# standard
from operator import index
from re import X
from turtle import width
import streamlit as st
from core.ThemePage import Page
import core.MultiApp as hub
from strlittemplate.util import Flattenjson, Value
# custom
import altair as alt
import pandas as pd
#####################
# main part
#####################


class Page3(Page):
    def __init__(self):
        super().__init__("Bar Chart", "Bar Chart", ['nothing to report'])

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

                if index1 != "none":
                    sort = st.checkbox("Sort?", value=False)
                    swap_axis = st.checkbox("Swap axis?", value=False)
                    value1, x_name = Value.GetCountDF(value1, index1)
                    if sort:
                        chart = alt.Chart(value1).mark_bar().encode(
                            alt.X(x_name + ':N', sort='y'),
                            alt.Y('count'))
                        if swap_axis:
                            chart = alt.Chart(value1).mark_bar().encode(
                                alt.Y(x_name + ':N', sort='x'),
                                alt.X('count'))

                    else:
                        chart = alt.Chart(value1).mark_bar().encode(
                            x=x_name, y='count')
                        if swap_axis:
                            chart = alt.Chart(value1).mark_bar().encode(
                                x='count', y=x_name)

                    rule = alt.Chart(value1).mark_rule(color='red').encode(
                        y='mean(count):Q'
                    )

                    if swap_axis:
                        rule = alt.Chart(value1).mark_rule(color='red').encode(
                            x='mean(count):Q'
                        )

                    st.altair_chart(
                        (chart +
                         rule).properties(
                            width=600,
                            height=500))
