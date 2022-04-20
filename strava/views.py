from django.shortcuts import render
from . api_service import *
from . analysis import *


def home_view(request):

    return render(request, 'home.html')


def analysis_view(request):
    user = request.user
    api_service = API_Service()
    data = api_service.get_data(user)
    activities = api_service.clean_data(data)
    analysis_service = Analysis()
    analysis = analysis_service.get_analysis(activities)
    context = analysis
    return render(request, 'analysis.html', context)


