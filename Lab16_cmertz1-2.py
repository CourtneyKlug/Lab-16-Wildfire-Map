#2.  Wildfire Map (Lab16_cmertz1-2)
#Courtney Mertz
#11/25/24

#This python file creates a map that points to places where wildfires have occured throughout the world
#with the help of data from a csv file. You can also adjust the num_rows to show a certain number amount,
#so that way the map is easier to read and the data can be better understood.

import csv
from datetime import datetime

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

#The world_fires_1_day.csv file has over 27,000 records, 
#so it's a good idea to make it so that only the 
#first 10,000 or 1,000 records are shown on the map.
#The map would be a mess to read data from otherwise!
num_rows = 1000

filename = 'world_fires_1_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get the brights, lats and lons, and dates.
    dates, brights = [], []
    lats, lons = [], []
    hover_texts = []
    row_num = 0
    for row in reader:
        date = datetime.strptime(row[5], '%Y-%m-%d')
        brightness = float(row[2])
        label = f"{date.strftime('%m/%d/%y')} - {brightness}"

        dates.append(date)
        brights.append(brightness)
        lats.append(row[0])
        lons.append(row[1])
        hover_texts.append(label)
        
        row_num += 1
        if row_num == num_rows:
            break

# Map the fires.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [brightness/20 for brightness in brights],
        'color': brights,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Brightness'},
    },
}]

my_layout = Layout(title='Global Fire Activity Map')

fig = {'data': data, 'layout': my_layout}
# Creates an html file for you to view the map at anytime, internet or not.
offline.plot(fig, filename='wildfire_map.html')