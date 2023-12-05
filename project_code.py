import streamlit as st
import pandas as pd
import altair as alt

prem_data = pd.read_csv('over0goal.csv')
st.dataframe(prem_data)
club_select = st.selectbox(prem_data['Current Club'].unique().tolist())
new_df = prem_data[prem_data['Current Club'] == club_select]

scatter=alt.Chart(new_df).mark_point().encode(
    x='club_list',
    y='count()'
)
st.altair_chart(scatter, use_container_width=True)
