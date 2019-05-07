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
    season_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    top_runs_bars = cg.top_runs_all_season()
    compound_chart = cg.top_runs_vs_teams()
    batsman_vs_team_chart = cg.batsman_vs_team('A Ashish Reddy', 'Chennai Super Kings')

    context = {
        'top_score_data': top_runs_bars.to_json(),
        'top_score_vs_team_data': compound_chart.to_json(),
        'batsman_vs_team_data': batsman_vs_team_chart.to_json(),
        'app_name': 'players',
        'player_list': player_list['Player_Name'].tolist(),
        'team_list': team_list['Team_Name'].tolist(),
        'season_list': season_list
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
    return JsonResponse(batsman_vs_season_chart.to_dict(), safe=False)
