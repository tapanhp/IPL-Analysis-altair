from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        'app_name': 'seasons'
    }
    return render(request, 'seasons/index.html', context)
