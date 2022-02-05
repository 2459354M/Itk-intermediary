from numpy import indices
import streamlit as st
from core.ThemePage import Page
import core.MultiApp as hub
# custom
import pandas as pd
#####################
# main part
#####################
def listkey(mylist,mykey,component=0):
    keys = [mykey]
    if type(mylist[mykey]) == dict:
        sub_key = st.selectbox("Select y component:", mylist[mykey],key=component)
        keys.extend(listkey(mylist[mykey],sub_key))
    elif type(mylist[mykey]) == list:
        sub_key = st.selectbox("Select y component:", range(len(mylist[mykey])),key=component)
        keys.extend(listkey(mylist[mykey],sub_key))
    return keys 

class Page1(Page):
    def __init__(self):
        super().__init__("pageC1", "Zeroth Page", ['nothing to report'])


    def main(self):
        pageDict = super().main()
        data = hub.App.get_data()
        if data:
            one_data = data[0]

            datakeys = one_data.keys()

            index1 = st.selectbox("Select y component:", datakeys)
            firstkey = listkey(one_data,index1,component=1)
            index2 = st.selectbox("Select x component:", datakeys)
            secondkey = listkey(one_data,index2,component=2)
        


