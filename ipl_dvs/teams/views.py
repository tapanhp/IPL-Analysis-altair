from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from . import chart_generator as cg
from . import data_reader as dr


# Create your views here.
def index(request):
    win_loss_chart = cg.win_loss()
    team_list = dr.teams['Team_Name'].tolist()
    total_runs = dr.total_runs.to_html(index=False)
    total_wickets = dr.total_wickets.to_html(index=False)
    wickets = dr.top_10_wicket[dr.top_10_wicket['team'] == 'Chennai Super Kings']
    wickets = wickets[['player', 'wickets']]
    team_vs_team = dr.team_vs_team[dr.team_vs_team['team'] == 'Chennai Super Kings']
    team_vs_team = team_vs_team[['vs', 'wins', 'losses']].to_html(index=False)
    context = {
        'app_name': 'teams',
        'team_win_loss_data': win_loss_chart.to_json(),
        'team_list': team_list,
        'total_runs_table': total_runs,
        'total_wickets_table': total_wickets,
        'top_ten_wickets_table': wickets.to_html(index=False),
        'team_vs_team_table': team_vs_team,
    }
    return render(request, 'teams/index.html', context)


@csrf_exempt
def update_top_wickets(request):
    team = request.POST['team']
    wickets = dr.top_10_wicket[dr.top_10_wicket['team'] == team]
    wickets = wickets[['player', 'wickets']].to_html(index=False)
    return JsonResponse(wickets, safe=False)


@csrf_exempt
def update_team_vs_team(request):
    team = request.POST['team']
    team_vs_team = dr.team_vs_team[dr.team_vs_team['team'] == team]
    team_vs_team = team_vs_team[['vs', 'wins', 'losses']].to_html(index=False)
    return JsonResponse(team_vs_team, safe=False)
