from django.http import JsonResponse
from django.shortcuts import render
import pandas as pd
from . import charts_generator as cg
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


def index(request):
    player_list = pd.read_csv('data_files/players.csv', delimiter=',')
    player_list.sort_values('Player_Name', inplace=True)
    team_list = pd.read_csv('data_files/teams.csv', delimiter=',')
    team_list.sort_values('Team_Name', inplace=True)
    season_list = pd.read_csv('data_files/player_season.csv', delimiter=',')
    season_list = season_list[season_list['player'] == 'A Ashish Reddy']
    season_list.sort_values('season', inplace=True)
    stadium_list = pd.read_csv('data_files/stadiums.csv', delimiter=',')
    top_10_wicket_table = pd.read_csv('data_files/top_10_wicket_takers.csv', delimiter=',')
    top_10_wicket_table = top_10_wicket_table.to_html(col_space=20, justify='left', index=False)
    stadium_list.sort_values('stadium', inplace=True)
    top_runs = pd.read_csv('data_files/Top_10_Runs_All_Seasons.csv', delimiter=',')
    top_runs.sort_values('Runs', ascending=False, inplace=True)
    top_runs = top_runs.head(10).to_html(col_space=20, justify='left', index=False)
    compound_chart = cg.top_runs_vs_teams()
    batsman_vs_team_chart = cg.batsman_vs_team('A Ashish Reddy', 'Chennai Super Kings')
    batsman_vs_season_chart = cg.batsman_vs_season('A Ashish Reddy', 5)
    batsman_vs_stadium_chart = cg.batsman_vs_stadium('A Ashish Reddy', 'Barabati Stadium')
    wickets_vs_teams_chart = cg.wickets_vs_teams('A Ashish Reddy')
    wickets_vs_season_chart = cg.wickets_vs_season('A Ashish Reddy')
    captain_win_loss_bar = cg.captains()

    context = {
        'top_runs': top_runs,
        'top_score_vs_team_data': compound_chart.to_json(),
        'batsman_vs_team_data': batsman_vs_team_chart.to_json(),
        'app_name': 'players',
        'player_list': player_list['Player_Name'].tolist(),
        'team_list': team_list['Team_Name'].tolist(),
        'season_list': season_list['season'].tolist(),
        'stadium_list': stadium_list['stadium'].tolist(),
        'batsman_vs_season_data': batsman_vs_season_chart.to_json(),
        'batsman_vs_stadium_data': batsman_vs_stadium_chart.to_json(),
        'top_10_wickets': top_10_wicket_table,
        'wickets_vs_team_data': wickets_vs_teams_chart.to_json(),
        'wickets_vs_season_data': wickets_vs_season_chart.to_json(),
        'captain_win_loss_data': captain_win_loss_bar.to_json()
    }
    return render(request, 'players/index.html', context)


@csrf_exempt
def update_batsman_vs_team(request):
    player = request.POST['player']
    team = request.POST['team']
    batsman_vs_team_chart = cg.batsman_vs_team(player, team)
    return JsonResponse(batsman_vs_team_chart.to_dict(), safe=False)


@csrf_exempt
def update_batsman_vs_season(request):
    player = request.POST['player']
    season = request.POST['season']
    batsman_vs_season_chart = cg.batsman_vs_season(player, season)
    # print(batsman_vs_season_chart.to_json())
    return JsonResponse(batsman_vs_season_chart.to_dict(), safe=False)


@csrf_exempt
def update_batsman_vs_stadium(request):
    player = request.POST['player']
    stadium = request.POST['stadium']
    batsman_vs_stadium_chart = cg.batsman_vs_stadium(player, stadium)
    return JsonResponse(batsman_vs_stadium_chart.to_dict(), safe=False)


@csrf_exempt
def update_wickets_vs_team(request):
    player = request.POST['player']
    wickets_vs_team_chart = cg.wickets_vs_teams(player)
    return JsonResponse(wickets_vs_team_chart.to_dict(), safe=False)


@csrf_exempt
def update_wickets_vs_season(request):
    player = request.POST['player']
    wickets_vs_season_chart = cg.wickets_vs_season(player)
    return JsonResponse(wickets_vs_season_chart.to_dict(), safe=False)


@csrf_exempt
def update_season_dropdown(request):
    player = request.POST['player']
    season_list = pd.read_csv('data_files/player_season.csv', delimiter=',')
    season_list = season_list[season_list['player'] == player]
    season_list.sort_values('season', inplace=True)
    return JsonResponse(season_list['season'].tolist(), safe=False)
