from django.shortcuts import render
from django.contrib.auth import get_user_model
from social_django.models import UserSocialAuth
import requests
import pandas as pd
from pandas import json_normalize
from . api_service import *
from . analysis import *
from . plot_generator import *
from plotly.offline import plot
import plotly.graph_objs as go
from plotly.graph_objs import Scatter
import plotly.express as px




# Create your views here.
def home_view(request):

    return render(request, 'home.html')


def analysis_view(request):
   #Get user into
    user = request.user
    api_service = API_Service()
    data = api_service.get_data(user)
    activities = api_service.clean_data(data)
    analysis_service = Analysis()
    analysis = analysis_service.get_analysis(activities)
    context = analysis

    return render(request, 'analysis.html', context)


