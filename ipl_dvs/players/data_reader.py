import pandas as pd

batsman_runs = pd.read_csv('data_files/batsman_runs.csv', delimiter=',')

top_runs = pd.read_csv('data_files/Top_10_Runs_All_Seasons.csv', delimiter=',')
top_runs.sort_values('Runs', ascending=False, inplace=True)

top_runs_vs_team = pd.read_csv('data_files/top_10_batsman_against_teams.csv', delimiter=',')
top_runs_vs_team.sort_values('runs', ascending=False, inplace=True)

wickets_against_a_team = pd.read_csv('data_files/wickets_against_team.csv', delimiter=',')
wickets_against_a_team.sort_values(['player', 'team'], inplace=True)

wickets_in_season = pd.read_csv('data_files/wickets_in_a_season.csv', delimiter=',')
wickets_in_season.sort_values(['player', 'season'], inplace=True)

captain_win_loss = pd.read_csv('data_files/captain_wins_loss.csv', delimiter=',')
# captain_win_loss.sort_values('team', inplace=True)


