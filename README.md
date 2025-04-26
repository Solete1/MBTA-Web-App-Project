Sneha Abinavam
Sol Troche-Rodrigo

# Project Overview 

For this project, we focused on creating a tool that users could use to search for MBTA stops. We generated three pages, each of which had a specific purpose:
    1. error.html: gave users a warning if they typed an incorrect MBTA station. There is a button that will take them to index.html to continue searching for a stop. 
    2. index.html: allows users to type in the name of the station they are looking for.
    3. mbta_station.html: this page shows the stop name, station's location, and if it is wheelchair accessible. 

For the three pages, we also added css to make it visually appealing. For index.html and mbta_station.html the color scheme was blue, but for the error.html page, we made it red to highlight the "mistake."

In order to support the "front-end" of the assignment, the "back-end" pages were app.py and mbta_helper.py. The latter was used to gather the information from Mapbox's API, while app.py collected all of the pieces of the project and brought it together in one page.

# Reflection

Overall, the project went smoothly. The work was divided between us in an equitable manner. Sneha created the foundation of the project with her code and special touches at the end, while Sol signed up for the APIs and finalised the code. At the same time that we were coding Assignment 3, we were also working on our Term Project, so when one person would be working on the code for one project, the other person would be working on the other assignment.

The main issues that we encountered was with the Mapbox API, leaking the .env, and incorrectly linking each page with each other. For the first two issues, Professor Li was a huge help. Meanwhile, for the last problem, it was relatively easy to figure out because of the hint provided in the error messages. Although there were other debugging issues, these three were the most concerning ones. 

Regarding the team dynamic, no obstacles were encountered. It helped a lot that we are friends and speak regularly, so we had the communication aspect perfected. For next time, the aspect that we could potentially improve on is having a clearer idea of what each person should be working on, so we are able to set the expectations and tasks since the beginning.

And lastly, we really enjoyed this project because it allowed us to further understand how the front-end and the back-end interact. AI also helped with questions we had about combining html and python for our end project. For example, ChatGPT was able to debug an issue that was impeding our html code from implementing the back-end from app.py (it ended up being a spelling error).
