# standard
import streamlit as st
from core.ThemePage import Page
import core.MultiApp as hub
# custom
import altair as alt
from strlittemplate.util import Dat_Parse
#####################
# main part
#####################


class Page2(Page):
    def __init__(self):
        super().__init__("Scatter Graph",
                         "Scatter Graph", ['nothing to report'])

    def main(self):
        pageDict = super().main()
        myfile = st.file_uploader("upload dat file")
        if myfile is not None:
            data, names = Dat_Parse.parse(myfile)
            graphscale = st.selectbox(
                "Scale:", ['linear', 'log', 'symlog'], index=0)
            colour_variable = st.selectbox(
                "Variable for colour:", names, index=0)
            chart = alt.Chart(data).mark_point().encode(
                alt.Y(names[1], scale=alt.Scale(type=graphscale)),
                x=names[0],
                color=colour_variable,
                tooltip=names
            ).interactive()

            st.altair_chart(
                (chart).properties(
                    width=600,
                    height=500))
