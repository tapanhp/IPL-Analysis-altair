from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        'app_name': 'teams'
    }
    return render(request, 'teams/index.html', context)
