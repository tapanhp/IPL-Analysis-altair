from django.shortcuts import render
from . import chart_generator as cg
from . import data_reader as dr


# Create your views here.
def index(request):
    win_loss_chart = cg.win_loss()
    team_list = dr.teams['Team_Name'].tolist()
    total_runs = dr.total_runs.to_html(index=False)
    context = {
        'app_name': 'teams',
        'team_win_loss_data': win_loss_chart.to_json(),
        'team_list': team_list,
        'total_runs_table': total_runs,
    }
    return render(request, 'teams/index.html', context)
