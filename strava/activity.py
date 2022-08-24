from . plot_generator import *

class Activity:
    def __init__(self, activity_data):
        self.build_activity_stats(activity_data)
    
    
    def build_activity_stats(self, activity_data):
        # assign all stats as instance attributes
        self.max_speed = max(activity_data['max_speed'])
        self.avg_speed = round(activity_data['average_speed'].mean(), 2)
        self.max_distance = max(activity_data['distance']) 
        self.avg_distance = round(activity_data['distance'].mean(), 2)
        self.max_elevation_gain = max(activity_data['total_elevation_gain'])
        pr_set = activity_data.loc[activity_data['pr_count']!=0] # get all entries with a pr
        if not pr_set.empty: 
            pr_date = pr_set[pr_set['start_date_local'] == pr_set['start_date_local'].max()] # get most recent date from pr entrires
            self.recent_pr = {'date': pr_date['start_date_local'].item(), 'name': pr_date['name'].item() }
        # add charts as instance attributes
        self.date_speed_chart = get_date_vs_avg_speed(activity_data)
        self.time_speed_chart = get_time_of_day_speed(activity_data)
        self.time_length_chart = get_time_of_day_length(activity_data)

    
    def to_dict(self):
        dict = {key:value for key, value in self.__dict__.items() if not key.startswith('__') and not callable(key)}
        return dict