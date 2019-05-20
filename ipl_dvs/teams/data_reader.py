import pandas as pd

win_loss = pd.read_csv('data_files/team_win_loss.csv', delimiter=',')

teams = pd.read_csv('data_files/teams.csv', delimiter=',')
teams.sort_values('Team_Name', inplace=True)

total_runs = pd.read_csv('data_files/team_total_runs.csv', delimiter=',')

total_wickets = pd.read_csv('data_files/team_total_wickets.csv', delimiter=',')

top_10_wicket = pd.read_csv('data_files/team_top_10_wicket_takers.csv', delimiter=',')

team_vs_team = pd.read_csv('data_files/team_vs_team_wins.csv', delimiter=',')

win_by_runs = pd.read_csv('data_files/win_by_runs.csv', delimiter=',')

win_by_wickets = pd.read_csv('data_files/win_by_wickets.csv', delimiter=',')

innings_and_wins = pd.read_csv('data_files/innings_and_wins.csv', delimiter=',')
