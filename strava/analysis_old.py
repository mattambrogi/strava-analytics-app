from .plot_generator import *



class Analysis():

    def get_analysis(self, activities):
        '''
            Takes cleaned activity data and returns a context dictionary which contains metrics and graphs to be displayed in UI.
            Generates metrics and graphs for up to three activities where the user has at least 5 data entries.
        '''
       
        def get_activity_stats(activity_data):
            '''
            Takes data from an indivudal activity and returns a dictionary with relevant summary statstics for that data.
            '''
            dict = {}
            dict['max_speed'] = max(activity_data['max_speed'])
            dict['avg_speed'] = round(activity_data['average_speed'].mean(), 2)
            dict['max_distance'] = max(activity_data['distance']) 
            dict['avg_distance'] = round(activity_data['distance'].mean(), 2)
            dict['max_elevation_gain'] = max(activity_data['total_elevation_gain'])
            pr_set = activity_data.loc[activity_data['pr_count']!=0] # get all entries with a pr
            if not pr_set.empty: 
                pr_date = pr_set[pr_set['start_date_local'] == pr_set['start_date_local'].max()] # get most recent date from pr entrires
                dict['recent_pr'] = {'date': pr_date['start_date_local'].item(), 'name': pr_date['name'].item() }
            return dict

        # create context dictionary for UI
        context = {}
 
        # add overview data to context
        activity_overview = dict(activities['type'].value_counts())
        context['overview'] = activity_overview
        context['overview_chart'] = get_overview_bar_chart(activity_overview)

        # add activitiy one data to context
        activity_one = activities['type'].value_counts().index[0]
        activity_one_data = activities.loc[activities['type'] == activity_one]
        context['activity_one'] = get_activity_stats(activity_one_data)
        context['activity_one']['name'] = activities['type'].value_counts().index[0]
        # add plots
        context['activity_one']['date_speed_chart'] = get_date_vs_avg_speed(activity_one_data)
        context['activity_one']['time_speed_chart'] = get_time_of_day_speed(activity_one_data)
        context['activity_one']['time_length_chart'] = get_time_of_day_length(activity_one_data)

        # add activitiy two data to context if it has at least 5 entries
        if list(activity_overview.values())[1] and list(activity_overview.values())[1] >= 5:
            activity_two = activities['type'].value_counts().index[1]
            activity_two_data = activities.loc[activities['type'] == activity_two]
            context['activity_two'] = get_activity_stats(activity_two_data)
            context['activity_two']['name'] = activities['type'].value_counts().index[1]
            # add plots
            context['activity_two']['date_speed_chart'] = get_date_vs_avg_speed(activity_two_data)
            context['activity_two']['time_speed_chart'] = get_time_of_day_speed(activity_two_data)
            context['activity_two']['time_length_chart'] = get_time_of_day_length(activity_two_data)

        # add activitiy three data to context if it has at least 5 entries
        if list(activity_overview.values())[2] and list(activity_overview.values())[2] >= 5:
            activity_three = activities['type'].value_counts().index[2]
            activity_three_data = activities.loc[activities['type'] == activity_three]
            context['activity_three'] = get_activity_stats(activity_three_data)
            context['activity_three']['name'] = activities['type'].value_counts().index[2]
            # add plots
            context['activity_three']['date_speed_chart'] = get_date_vs_avg_speed(activity_three_data)
            context['activity_three']['time_speed_chart'] = get_time_of_day_speed(activity_three_data)
            context['activity_three']['time_length_chart'] = get_time_of_day_length(activity_three_data)

        return context




 





