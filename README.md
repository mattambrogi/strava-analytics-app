# strava-analytics-app
A web app that provides Strava users with insights and analysis of their activities. You can visit [the live app](https://my-strava-data.herokuapp.com/), or watch a [demo](https://www.mattambrogi.com/posts/strava-analysis/).


## What is it
This is a web app built for athletes who use the app [Strava](https://www.strava.com/) to track activities such as running, cycling, and hiking. The app allows users see a report of key stats and trends for each of their top three Strava activities. Users's just need to visit the landing page, authenticate their Strava profile, and will then be taken to the report generated from their data. 


## Why I built it
Strava withholds most insights for paying subscribers. A while back I wrote an article about how to use Python to pull data from the Strava API and analyze it. I got a lot of inbound interest after publishing the article. Others wanted to see the same analysis, but were not familiar with Python, accessing data from APIs, Pandas, or many of the other tools I used. 

During Recurse Center, I decided to build a web app that would generate this analysis for others without them having to do any work. 


## Features
- Users can visit the landing page and then connect their Strava account through OAuth at the click of a button.
- Users are then shown a report which contains stats and charts providing an overview of their activities, as well as a deep dive into each of their top three activities.
- The deep dives contain the following information:
  - Max speed
  - Average speed
  - Longest
  - Average length
  - Max elevation gain
  - Date of last personal record
  - Average speed vs Date (chart)
  - Average speed vs Time of Day (chart)
  - Distance vs Time of Day (chart)


## Technologies
- Python
- Django
- Django Social Auth
- Pandas
- Plotly
- HTML, CSS, Bootstrap frontend
- Heroku deployment


## Future work


### Features
If I carve out more time to work on this in the future, there are a number of features I would add.
- Error handling
  - There is minimal error handling or messaging built into the project. For example, a user may be able to connect their Strava acccount, but if they don't have at least five data points for a given activity, they will not see any analysis. Even through this is noted on the landing page, this could still happen. If so, the user should be displayed a message that communciates why.
- Tests
  - I would like to add tests for the analysis service. Given controlled input data, does it output the stats I would expect?
- Trendlines for charts
  - I would like users to see trendlines on their charts. This turns out to be tricky because the optimal trendline depends on how many data points a user has. I.e. a linear trendline may be most informative if a user has a high number of recorded activities, but useless with fewer. There are also technical hurdles when creating trendlines with dates on the x axis in plotly. 
- Google OAuth bug
  - There is a bug that prevents users from authenticating their Strava account if they signed up with Strava via Google. This seems to be a bug on the Google side, but I would like to explore it further given the time. 

There are also a handful of features that I would classify as nice to haves:
- The ability to download a report
- The ability to share a report
- The ability to make an account, save, and track metrics over time


## Reflections
This project taught me a lot. I explored program design and separation of concerns. I learned a great deal about OAuth. I learned how to run, and present, analysis from the backend. 

More generally, I am interested in building tools that help others learn from and explore data. This was a great exercise in that. 
