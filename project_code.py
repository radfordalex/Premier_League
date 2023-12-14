import streamlit as st
import pandas as pd
import altair as alt

# prem_data = pd.read_csv('over0goal.csv')
# prem_data_copy = prem_data.copy()
# club_list = prem_data['Current Club'].unique().tolist()

column_rename_mapping = {
    'full_name': 'Player Name',
    'age': 'Age',
    'position': 'Position',
    'Current Club': 'Current Club',
    'minutes_played_overall': 'Total Minutes Played',
    'minutes_played_home': 'Minutes Played at Home',
    'minutes_played_away': 'Minutes Played Away',
    'nationality': 'Nationality',
    'appearances_overall': 'Total Appearances',
    'appearances_home': 'Home Appearances',
    'appearances_away': 'Away Appearances',
    'goals_overall': 'Total Goals',
    'goals_home': 'Home Goals',
    'goals_away': 'Away Goals',
    'assists_overall': 'Total Assists',
    'assists_home': 'Home Assists',
    'assists_away': 'Away Assists',
    'penalty_goals': 'Penalty Goals',
    'penalty_misses': 'Penalty Misses',
    'clean_sheets_overall': 'Total Clean Sheets',
    'clean_sheets_home': 'Home Clean Sheets',
    'clean_sheets_away': 'Away Clean Sheets',
    'conceded_overall': 'Goals Conceded Overall',
    'conceded_home': 'Goals Conceded at Home',
    'conceded_away': 'Goals Conceded Away',
    'yellow_cards_overall': 'Total Yellow Cards',
    'red_cards_overall': 'Total Red Cards',
    'goals_involved_per_90_overall': 'Goals Involved Per 90 Minutes',
    'assists_per_90_overall': 'Assists Per 90 Minutes',
    'goals_per_90_overall': 'Goals Per 90 Minutes',
    'goals_per_90_home': 'Home Goals Per 90 Minutes',
    'goals_per_90_away': 'Away Goals Per 90 Minutes',
    'min_per_goal_overall': 'Minutes Per Goal Overall',
    'conceded_per_90_overall': 'Goals Conceded Per 90 Minutes',
    'min_per_conceded_overall': 'Minutes Per Goal Conceded',
    'min_per_match': 'Minutes Per Match',
    'min_per_card_overall': 'Minutes Per Card',
    'min_per_assist_overall': 'Minutes Per Assist',
    'cards_per_90_overall': 'Cards Per 90 Minutes',
    'rank_in_club_top_scorer': 'Rank in Club as Top Scorer'
}

@st.cache_resource
def load_data():
    # Load the dataset from a CSV file.
    df = pd.read_csv('over0goal.csv')
    # Drop the unwanted columns.
    df.drop(['Unnamed: 0', 'birthday_GMT'], axis=1, inplace=True)
    # Rename columns
    df.rename(columns=column_rename_mapping, inplace=True)
    return df

# Load your data
data = load_data()

st.title('2020/2021 Premier League Player Statistics')
st.text('Who was the most efficient Goal Scorer of the 2020/2021 Premier League Season?')

selected_names = st.multiselect('Select Premier League Players for Comparison', data['Player Name'].unique())
select_measure = [
    'Total Assists',
    'Total Minutes Played',
    'Total Appearances',
    'Minutes Per Match',
    'Cards Per 90 Minutes',
    'Club Top Scorer Rank'
]

select_measure_bar = [
    'Total Goals',
    'Total Assists',
    'Total Minutes Played',
    'Total Appearances',
    'Minutes Per Match',
    'Cards Per 90 Minutes',
    'Club Top Scorer Rank'
]

# Filter data based on the selected club and names
filtered_data = data[(data['Player Name'].isin(selected_names))]

tab1, tab2 = st.tabs(['Scatter Plot', 'Bar Chart'])

with tab1:
    st.sidebar.header('Scatterplot Options')
    y_axis = st.sidebar.selectbox('Pick your y-axis', select_measure)
    
    if selected_names:  # Check if there are any names selected
        st.dataframe(filtered_data)
        
        # Check if filtered_data is not empty
        if not filtered_data.empty:
            # Compute the min and max values with some padding for the X and Y axes
            padding = 1  # This is an arbitrary padding value you can adjust
            x_min = filtered_data['Total Goals'].min() - padding
            x_max = filtered_data['Total Goals'].max() + padding
            y_min = filtered_data[y_axis].min() - padding
            y_max = filtered_data[y_axis].max() + padding

            # Create the scatter plot
            scat_w_tooltip = alt.Chart(filtered_data, title=f'Goals versus {y_axis}').mark_circle(size=60).encode(
                alt.X('Total Goals', scale=alt.Scale(domain=(x_min, x_max))),
                alt.Y(y_axis, title=f'{y_axis}', scale=alt.Scale(domain=(y_min, y_max))),
                tooltip=['Player Name', 'Age', 'Current Club', 'Nationality', 'Position', 'Total Goals', y_axis]
            ).configure_mark(
                opacity=0.8,
                color='red',
                filled=False
            ).interactive()

            st.altair_chart(scat_w_tooltip, use_container_width=True)
        else:
            st.warning("Please select at least one player to display the scatter plot.")
    else:
        st.info("Select players to see the scatter plot.")



with tab2:
    st.sidebar.header('Bar Chart Options')
    bar_stat = st.sidebar.selectbox('Pick your Stat', select_measure_bar)
    count = st.sidebar.number_input(f'Top/Bottom N {bar_stat}', min_value=1, max_value=100, value=20, step=1)

    # Radio button for choosing Top or Bottom N
    top_or_bottom = st.sidebar.radio("Choose Top or Bottom", ('Top', 'Bottom'))

    # Conditional logic for Top or Bottom N
    if top_or_bottom == 'Top':
        display_data = data.nlargest(count, bar_stat)
    else:
        display_data = data.nsmallest(count, bar_stat)

    # Create the bar chart
    bar_chart = alt.Chart(display_data).mark_bar().encode(
        y=alt.Y('Player Name', title='Player Name', sort='-x'),
        x=alt.X(bar_stat, title=bar_stat),
        tooltip=['Player Name', bar_stat]
    )

    st.altair_chart(bar_chart, use_container_width=True)