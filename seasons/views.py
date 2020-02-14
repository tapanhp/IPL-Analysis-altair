from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from . import data_reader as dr


# Create your views here.
def index(request):
    top_runs = dr.top_runs.to_html(index=False)
    top_wickets = dr.top_wickets.to_html(index=False)
    team_wins = dr.team_wins[dr.team_wins['season'] == 1][['team', 'wins']].sort_values('wins', ascending=False).to_html(index=False)
    context = {
        'app_name': 'seasons',
        'top_runs': top_runs,
        'top_wickets': top_wickets,
        'team_wins': team_wins,
    }
    return render(request, 'seasons/index.html', context)


@csrf_exempt
def update_team_wins(request):
    season = request.POST['season']
    team_wins = dr.team_wins[dr.team_wins['season'] == int(season)][['team', 'wins']].sort_values('wins', ascending=False).to_html(
        index=False)
    return JsonResponse(team_wins, safe=False)
