import json
import streamlit as st
from core.ThemePage import Page
import core.MultiApp as hub
from strlittemplate.util import Flattenjson, Value
# custom
import numpy as np
import pandas as pd
import plotly.express as px
#####################
# main part
#####################


class Page1(Page):
    def __init__(self):
        super().__init__(
            "Pie Charts and Sunburst",
            "Pie Charts and Sunburst",
            ['nothing to report'])

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

            index1 = st.selectbox("Select y component:", stringkeys, index=0)

            value1, value2 = [], []
            if index1 != "none":
                for i in data:
                    value1.append(Value.getValue(
                        i, flatdatakeys, index1))
                index2 = st.selectbox(
                    "Select x component:", stringkeys, index=0)
                if index2 != "none":
                    for i in data:
                        value2.append(Value.getValue(
                            i, flatdatakeys, index2))
                if index2 == "none":
                    value1 = Value.count(value1)
                    filter = st.slider("""Select point at which
                                     to disregard component:""",
                                       min_value=0,
                                       max_value=max(value1.values()),
                                       value=0)
                    value1 = {k: v for k, v in value1.items() if v > filter}
                    chart = px.pie(values=list(value1.values()),
                                   names=value1.keys())
                    st.plotly_chart(chart)
                elif index2 != "none":
                    try:
                        df = pd.DataFrame({"value1": value1, "value2": value2})
                        chart = px.sunburst(df, path=["value2", "value1"])
                        st.plotly_chart(chart)

                    except BaseException:
                        st.write("invalid sunburst config")
