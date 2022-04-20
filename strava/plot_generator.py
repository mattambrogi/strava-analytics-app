from plotly.offline import plot
import plotly.graph_objs as go
from plotly.graph_objs import Scatter
import plotly.express as px
import pandas as pd
import datetime as dt



def get_date_vs_avg_speed(activity):
    df = activity
    # changes date into distance from an arbirary past date, done for plotting purposed
    df['serialized_date'] = [(d - dt.date(1970,1,1)).days for d in df['start_date_local']]
    fig = px.scatter(df, x="start_date_local", y="average_speed", height=500,
    labels={
            "start_date_local": "Date",
            "average_speed": "Average Speed",
        },
        title="Average Speed over Time")
    fig.update_layout(title_x=0.5, font_family="Roboto Mono", margin=dict(l=5, r=5),)
    fig.update_yaxes(title=None)
    plot_div = plot(fig, output_type='div')
    return plot_div

def get_overview_bar_chart(activity_overview):
    df = activity_overview
    x_data = list(activity_overview.keys())
    y_data = list(activity_overview.values())
    fig = px.bar(y=x_data, x=y_data, orientation='h', height=400, labels={
            'x': "Count",
            'y': "",
        })
    fig.update_yaxes(autorange="reversed", title=None,) 
    fig.update_layout(font_family="Roboto Mono", margin=dict(l=5, r=5),)
    plot_div = plot(fig, output_type='div')
    return plot_div

def get_time_of_day_speed(activity):
    x_data = activity['start_time'].tolist()
    y_data = activity['average_speed'].tolist()
    for index, time in enumerate(x_data):
        x_data[index] = dt.datetime.combine(dt.date(2022, 1, 1), time)
    fig = px.scatter(x=x_data, y=y_data, height=500, 
    labels={
            "x": "Time of day",
            "y": "Average Speed",
        },
        title="Average Speed vs Time of Day")
    fig.update_layout(title_x=0.5, font_family="Roboto Mono", margin=dict(l=5, r=5),)
    fig.update_xaxes(type='date', 
                tickformat='%H:%M', 
                nticks=24, 
                range=[min(x_data),max(x_data)])
    fig.update_yaxes(title=None)
    plot_div = plot(fig, output_type='div')
    return plot_div

def get_time_of_day_length(activity):
    x_data = activity['start_time'].tolist()
    y_data = activity['distance'].tolist()
    for index, time in enumerate(x_data):
        x_data[index] = dt.datetime.combine(dt.date(2022, 1, 1), time)
    fig = px.scatter(x=x_data, y=y_data, height=500, 
    labels={
            "x": "Time of day",
            "y": "Distance",
        },
        title="Distance vs Time of Day")
    fig.update_layout(title_x=0.5, font_family="Roboto Mono", margin=dict(l=5, r=5),)
    fig.update_xaxes(type='date', 
                tickformat='%H:%M', 
                nticks=24, 
                range=[min(x_data),max(x_data)])
    fig.update_yaxes(title=None)
    plot_div = plot(fig, output_type='div')
    return plot_div

# Start time frequency not currently displayed in UI
def get_start_freq(activity):
    x_data = activity['start_time'].tolist()
    for index, time in enumerate(x_data):
        x_data[index] = dt.datetime.combine(dt.date(2022, 1, 1), time)
    fig = px.histogram(x=x_data, labels={
            "x": "Time of day",
        },
        title="Frequency of Start Times")
    fig.update_xaxes(type='date', 
                tickformat='%H:%M', 
                range=[min(x_data),max(x_data)])
    fig.update_layout(bargap=0.2, title_x=0.5)
    plot_div = plot(fig, output_type='div')
    return plot_div

    

    
