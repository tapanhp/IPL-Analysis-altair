import pandas as pd

batsman_vs_team = pd.read_csv('data_files/batsman_vs_team.csv', delimiter=',')


top_runs = pd.read_csv('data_files/Top_10_Runs_All_Seasons.csv', delimiter=',')
top_runs.sort_values('Runs', ascending=False, inplace=True)

top_runs_vs_team = pd.read_csv('data_files/top_10_batsman_against_teams.csv', delimiter=',')
top_runs_vs_team.sort_values('runs', ascending=False, inplace=True)
