from social_django.models import UserSocialAuth
import requests
import pandas as pd
from pandas import json_normalize


class API_Service():

    def get_data(self, user): #add optional request param
        strava_login = user.social_auth.get(provider='strava')
        access_token = strava_login.extra_data['access_token']
        #Make API Call
        activites_url = "https://www.strava.com/api/v3/athlete/activities"
        header = {'Authorization': 'Bearer ' + access_token}
        param = {'per_page': 200, 'page': 1}
        #Load data
        data = requests.get(activites_url, headers=header, params=param).json()
        return data

    def clean_data(self, data):
        activities = json_normalize(data)
        #Create new dataframe with select columns
        cols = ['name', 'upload_id', 'type', 'distance', 'moving_time',   
                'average_speed', 'max_speed','total_elevation_gain',
                'start_date_local', 'pr_count'
            ]
        activities = activities[cols]
        #Break date into start time and date
        activities['start_date_local'] = pd.to_datetime(activities['start_date_local'])
        activities['start_time'] = activities['start_date_local'].dt.time
        activities['start_date_local'] = activities['start_date_local'].dt.date
        #Change km/hr to mph
        activities['max_speed'] = round(activities['max_speed'] * 2.237, 2)
        activities['average_speed'] = round(activities['average_speed']* 2.237, 2)
        #Change meters to miles
        activities['distance'] = round(activities['distance'] / 1609.34, 2)
        # Convert meters to feet
        activities['total_elevation_gain'] = round(activities['total_elevation_gain'] * 3.28)
        
        return activities






