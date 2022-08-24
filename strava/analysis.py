from .plot_generator import *
from .activity import Activity


def get_analysis(activities):
    # create high level context dict for templates 
    context_dict = {}
    context_dict['activities'] = []

    # get high level acitivites overview data
    activity_overview = dict(activities['type'].value_counts())
    # append overview data to context
    context_dict['overview'] = activity_overview
    context_dict['overview_chart'] = get_overview_bar_chart(activity_overview)

    # build activity data for top 3 activities with at least 5 entries and append to context
    for i in range(3):
        # if activity exists and has at least 5 entries
        if list(activity_overview.values())[0] and list(activity_overview.values())[0] >= 5:
            # get activity data
            activity = activities['type'].value_counts().index[i]
            activity_data = activities.loc[activities['type'] == activity]
            # initalize activity object, this will also build stats and charts
            activity = Activity(activity_data)
            # add name and rank attributes
            activity.name = activities['type'].value_counts().index[i]
            activity.rank = i+1
            # append to context for template
            context_dict['activities'].append(activity)

    return context_dict


