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
    print(wickets)
    context = {
        'app_name': 'teams',
        'team_win_loss_data': win_loss_chart.to_json(),
        'team_list': team_list,
        'total_runs_table': total_runs,
        'total_wickets_table': total_wickets,
        'top_ten_wickets_table': wickets.to_html(index=False),
    }
    return render(request, 'teams/index.html', context)


@csrf_exempt
def update_top_wickets(requset):
    team = requset.POST['team']
    wickets = dr.top_10_wicket[dr.top_10_wicket['team'] == team]
    wickets = wickets[['player', 'wickets']].to_html(index=False)
    return JsonResponse(wickets, safe=False)
