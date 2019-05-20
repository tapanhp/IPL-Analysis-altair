from django.shortcuts import render
from . import data_reader as dr


# Create your views here.
def index(request):
    top_runs = dr.top_runs.to_html(index=False)
    top_wickets = dr.top_wickets.to_html(index=False)
    context = {
        'app_name': 'seasons',
        'top_runs': top_runs,
        'top_wickets': top_wickets,
    }
    return render(request, 'seasons/index.html', context)
