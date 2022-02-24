import itertools
import json
from re import S
from git import TagReference
import streamlit as st
from core.ThemePage import Page
import core.MultiApp as hub
from strlittemplate.util import Flattenjson, Value
# custom
import numpy as np
import pandas as pd
import plotly.graph_objects as go
#####################
# main part
#####################


class Page2(Page):
    def __init__(self):
        super().__init__("Sankey", "Sankey", ['nothing to report'])

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

                    mylist = value1.copy()
                    mylist.extend(value2)
                    mylist = list(set(mylist))
                    source = []
                    for i in value1:
                        source.append(mylist.index(i))

                    target = []
                    for i in value2:
                        target.append(mylist.index(i))

                    a = zip(source, target)

                    d = Value.count(a)
                    source, target, value = [], [], []
                    for i in d.keys():
                        source.append(i[0])
                        target.append(i[1])
                        value.append(d[i])

                    data = [go.Sankey(node=dict(
                        pad=15,
                        thickness=20,
                        line=dict(color="black", width=0.5),
                        label=mylist,
                        color="blue"
                    ),
                        link=dict(source=source, target=target, value=value))]
                    st.plotly_chart(data)
