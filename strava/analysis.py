




class Analysis():

    def get_analysis(self, activities):
        context = {}
        activity_overview = dict(activities['type'].value_counts())
        activity_one = activities['type'].value_counts().index[0]
        activity_one_data = activities.loc[activities['type'] == activity_one] 
        activity_two = activities['type'].value_counts().index[1]
        activity_two_data = activities.loc[activities['type'] == activity_two] 

        def get_activity_stats(activity_data):
            dict = {}
            dict['max_speed'] = max(activity_data['max_speed'])
            dict['avg_speed'] = round(activity_data['average_speed'].mean(), 2)
            dict['max_distance'] = max(activity_data['distance']) 
            dict['avg_distance'] = round(activity_one_data['distance'].mean(), 2)
            dict['max_elevation_gain'] = max(activity_data['total_elevation_gain'])
            pr_set = activity_data.loc[activity_data['pr_count']!=0]
            pr_date = pr_set[pr_set['start_date_local'] == pr_set['start_date_local'].max()]
            dict['recent_pr'] = {'date': pr_date['start_date_local'].item(), 'name': pr_date['name'].item() }
            return dict


        context['overview'] = activity_overview
        context['activity_one'] = get_activity_stats(activity_one_data)
        context['activity_one']['name'] = activities['type'].value_counts().index[0]
        context['activity_two'] = get_activity_stats(activity_two_data)
        context['activity_two']['name'] = activities['type'].value_counts().index[1]

        return context




 





