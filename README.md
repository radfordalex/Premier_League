# Streamlit Application
https://premier-league-goal-scorers.streamlit.app/

# Premier League Goal Scorer Efficiency 
This Streamlit application is designed to visualize and analyze statistics of Premier League players from the 2020/2021 season. The problem it aims to solve is the lack of an interactive platform where fans, analysts, or interested parties can select specific players to compare and contrast various player-level statistics (assists, minutes played, appearances, etc) against goals scored (player-level) so users can identify the most efficient and effective goal scorers during the 2020/2021 season. The app tells the story of player performance and allows users to gain insights into the data through visual exploration. The question we're interested in: Who is the most efficient goal scorer during the 2020/2021 Premier League Season?

# Data/Operation Abstract Design
The data for this application was sourced from a CSV file containing detailed player statistics for all players with more than 1 goal and over 90 minutes (one full game) played for the 2020/2021 Premier League season. The data preparation involved dropping unnecessary columns, renaming columns for clarity, and filtering data based on user inputs such as player name selection.

# Future Work
Data Updates - Implement a way to update dataset (such as integrating with external APIs) with new statistics to enrich the dataset by allowing the app to cover more seasons or utilize more real-time data like player injuries, transfers, etc.
User Customization - Allow users to create custom metrics or combine existing ones for deeper analysis
Enhanced Interactivity - Introduce more interactive elements such as player comparison sliders, dynamic filtering, and the ability to track changes over time with a time slider for different seasons