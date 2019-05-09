import pandas as pd

win_loss = pd.read_csv('data_files/team_win_loss.csv', delimiter=',')

teams = pd.read_csv('data_files/teams.csv', delimiter=',')
teams.sort_values('Team_Name', inplace=True)

total_runs = pd.read_csv('data_files/team_total_runs.csv', delimiter=',')
