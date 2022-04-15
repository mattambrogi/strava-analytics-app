from plotly.offline import plot
import plotly.graph_objs as go
from plotly.graph_objs import Scatter
import plotly.express as px
import pandas as pd
import datetime as dt





def get_plots(activities):
    activity_one = activities['type'].value_counts().index[0]
    activity_one_data = activities.loc[activities['type'] == activity_one] 
    activity_two = activities['type'].value_counts().index[1]
    activity_two_data = activities.loc[activities['type'] == activity_two] 
    activity_overview = dict(activities['type'].value_counts())

    def get_date_vs_avg_speed(activity):
        df = activity
        df['serialized_date'] = [(d - dt.date(1970,1,1)).days for d in df['start_date_local']]

        fig = px.scatter(df, x="start_date_local", y="average_speed", height=500,
        labels={
                "start_date_local": "Date",
                "average_speed": "Average Speed",
            },
            title="Average Speed over Time")
        fig.update_layout(title_x=0.5, font_family="Roboto Mono", margin=dict(l=5, r=5),)
        fig.update_yaxes(title=None)
        #fig.update_xaxes(tickvals= df['serialized_date'][0::5], ticktext = df['start_date_local'][0::5])
        # Add trendline
        #fig.add_traces(list(px.scatter(x=df['start_date_local_2'], y=df['average_speed'], trendline="lowess", trendline_options=dict(frac=0.3), height=500,).select_traces()))
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
        #activity['start_time'] = dt.datetime.combine(dt.date(2022,1,1), activity['start_time'] )
        #above didn't work because can't do to series, need to do indivudually
        x_data = activity['start_time'].tolist()
        y_data = activity['average_speed'].tolist()
        for index, time in enumerate(x_data):
            x_data[index] = dt.datetime.combine(dt.date(2022, 1, 1), time)
        #df['start_date_local_2'] = [(d - dt.date(1970,1,1)).days for d in df['start_date_local']]

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
                    #range=[dt.datetime(2022, 1, 1, 7, 0),dt.datetime(2022, 1, 1, 23, 00)]) #7 to 11, could dyanimcally set
                    range=[min(x_data),max(x_data)])
        fig.update_yaxes(title=None)
        plot_div = plot(fig, output_type='div')
        return plot_div
    
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

        

    
    
    additional_context = {}
    additional_context['overview_chart'] = get_overview_bar_chart(activity_overview)
    additional_context['date_speed_chart_1'] = get_date_vs_avg_speed(activity_one_data)
    additional_context['date_speed_chart_2'] = get_date_vs_avg_speed(activity_two_data)
    additional_context['time_speed_chart_1'] = get_time_of_day_speed(activity_one_data)
    additional_context['time_speed_chart_2'] = get_time_of_day_speed(activity_two_data)
    additional_context['start_freq_2'] = get_start_freq(activity_two_data)


    return additional_context
