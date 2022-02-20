from email.policy import default
from matplotlib.pyplot import get
import streamlit as st
from core.ThemePage import Page
import core.MultiApp as hub
from strlittemplate.util import Flattenjson, Value
# custom
import numpy as np
import pandas as pd
#####################
# main part
#####################


class Page1(Page):
    def __init__(self):
        super().__init__("pageC1", "Zeroth Page", ['nothing to report'])

    def main(self):
        pageDict = super().main()
        data = hub.App.get_data()
        if data:
            one_data = data[0]

            flatdatakeys = Flattenjson.flattenjson(one_data)
            stringkeys = list(flatdatakeys.keys())
            stringkeys.insert(0, "none")

            index1 = st.selectbox("Select y component:", stringkeys, index=0)
            index2 = st.selectbox("Select x component:", stringkeys, index=0)

            value1, value2 = [], []
            if index1 != "none" and index2 != "none":
                for i in range(len(data)):
                    value1.append(Value.getValue(
                        data[i], flatdatakeys, index1))
                    value2.append(Value.getValue(
                        data[i], flatdatakeys, index2))
                st.write(Value.count(value1))
                st.write(Value.count(value2))
