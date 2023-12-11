import streamlit as st
import pandas as pd
import altair as alt

prem_data = pd.read_csv('over0goal.csv')
prem_data_copy = prem_data.copy()
club_list = prem_data['Current Club'].unique().tolist()

st.title('2020/2021 Premier League Goal Scorer Statistics')
st.text('Vizualizations of statistics related to Top Goal Scorers of 2020/2021 Premier League Season')
#club_select = st.selectbox('Select Premier League Club', club_list)
#new_df = prem_data[prem_data['Current Club'] == club_select]
#prem_data['club_select'] = prem_data['Current Club'] == club_select
#st.dataframe(prem_data)
#st.dataframe(new_df)

selected_names = st.multiselect('Select Players (Multiselect)', prem_data['full_name'].unique())

# Filter data based on the selected club and names
filtered_data = prem_data[(prem_data['full_name'].isin(selected_names))]

# Display the filtered DataFrame
st.dataframe(filtered_data)

# Create Altair chart for the filtered data
scat_w_tooltip = alt.Chart(filtered_data).mark_circle(size=60).encode(
    x='goals_overall',
    y='minutes_played_overall',
    tooltip=['full_name', 'nationality', 'position', 'age']
).interactive()
# Filter data based on the selected club for the Altair chart
# filtered_data = prem_data[prem_data['Current Club'] == club_select]

# scat_w_tooltip = alt.Chart(filtered_data).mark_circle(size=60).encode(
#     x='goals_overall',
#     y='minutes_played_overall',
#     tooltip=['full_name', 'nationality', 'position', 'age']
# ).interactive()

# st.altair_chart(scat_w_tooltip, use_container_width=True)

# scatter=alt.Chart(prem_data).mark_point().encode(
#     x= 'club_select',
#     y='count()'
# )
#st.altair_chart(scatter, use_container_width=True)

# scat_w_tooltip = alt.Chart(prem_data).mark_circle(size=60).encode(
#     x='goals_overall',
#     y='minutes_played_overall',
#     color='Current Club',
#     tooltip=['full_name', 'Current Club', 'nationality', 'position', 'age']
# ).interactive()

# st.altair_chart(scat_w_tooltip, use_container_width=True)
