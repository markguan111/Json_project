import json

infile = open('eq_data_1_day_m1.json', 'r')
outfile = open('readable_eq_data.json', 'w')

eqdata = json.load(infile)

json.dump(eqdata, outfile, indent=4)


print(len(eqdata["features"]))

list_of_eqs = eqdata["features"]


mags = []
lats = []
lons = []

for eq in list_of_eqs:
    mag = eq['properties']['mag']
    mags.append(mag)
    lat = eq['geometry']['coordinates'][0]
    lon = eq['geometry']['coordinates'][1]
    lats.append(lat)
    lons.append(lon)


print(lats)
print(lons)

print(mags)
