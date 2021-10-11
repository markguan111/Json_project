from plotly import offline
from plotly.graph_objs import Scattergeo, Layout
import json

infile = open('US_fires_9_14.json', 'r')
outfile = open('readable_9_14_data.json', 'w')

fire2data = json.load(infile)

json.dump(fire2data, outfile, indent=4)

lats, lons, brightness = [], [], []

for fires in fire2data:
   
    if fires["brightness"] > 450:
        lat = fires["latitude"]
        lon = fires["longitude"]
        bri = fires["brightness"]
        lats.append(lat)
        lons.append(lon)
        brightness.append(bri)


data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker': {
        'size': [0.04*m for m in brightness],
        'color':brightness,
        'colorscale':'Viridis',
        'reversescale': True,
        'colorbar':{'title': 'brightness'}
    }
}]

my_layout = Layout(title="US Fires - 9/14/2020 through 9/20/2020")

fig = {'data': data, 'layout': my_layout}

offline.plot(fig, filename='US_fires_9_14.html')
