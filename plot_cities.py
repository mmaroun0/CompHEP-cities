import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

cities = [["Chicago",41.8781, -87.6298],
          ["Boston", 42.3555, -71.0565],
          ["New York", 40.7128, -74.0060],
          ["Los Angeles", 34.0522, -118.2437],
          ["San Francisco", 37.7749, -122.4194],
          ["Seattle", 47.6062, -122.3321],
          ["Miami", 25.7617, -80.1918],
          ["Houston", 29.7604, -95.3698],
          ["Phoenix", 33.4484, -112.0740],
          ["Denver", 39.7392, -104.9903],
          ["Providence", 41.8240, -71.4128],
          ["Baltimore", 39.2904, -76.6122],
          ["Atlanta", 33.7490, -84.3880],
          ["Washington", 38.9072, -77.0369],
          ["Dallas", 32.7767, -96.7970],
          ["San Diego", 32.7157, -117.1611],
          ["Orlando", 28.5383, -81.3792],
          ["Charlotte", 35.2271, -80.8431],
          ["Nashville", 36.1627, -86.7816],
          ["Minneapolis", 44.9778, -93.2650],
          ["Portland", 45.5051, -122.6750],
          ["Las Vegas", 36.1699, -115.1398],
          ["Salt Lake City", 40.7608, -111.8910],
          ["Milwaukee", 43.0389, -87.9065],
          ["Cincinnati", 39.1031, -84.5120],
          ["Kansas City", 39.0997, -94.5786],
          ["St. Louis", 38.6270, -90.1994],
          ["Pittsburgh", 40.4406, -79.9959],
          ["Cleveland", 41.4995, -81.6954],
          ["Indianapolis", 39.7684, -86.1581],
          ["Columbus", 39.9612, -82.9988],
          ["Omaha", 41.2565, -95.9345],
          ["Louisville", 38.2527, -85.7585],
          ["Tampa", 27.9506, -82.4572],
          ["Raleigh", 35.7796, -78.6382],
          ["Milwaukee", 43.0389, -87.9065],
          ["Albuquerque", 35.0844, -106.6504],
          ["Virginia Beach", 36.8529, -75.9780],
          ["Atlanta", 33.7490, -84.3880],
          ["Oklahoma City", 35.4676, -97.5164],
          ["New Orleans", 29.9511, -90.0715],
          ["Birmingham", 33.5207, -86.8025],
          ["Jacksonville", 30.3322, -81.6557],
          ["Memphis", 35.1495, -90.0490],
          ["Tulsa", 36.1539, -95.9928],
          ["Wichita", 37.6872, -97.3301],
          ["Fresno", 36.7378, -119.7871],
          ["Long Beach", 33.7701, -118.1937],
          ["Kansas City", 39.0997, -94.5786],
          ["Omaha", 41.2565, -95.9345],
          ["Virginia Beach", 36.8529, -75.9780],
          ["Amherst", 42.3757, -72.5199]]
        
scale = 5

map = Basemap(llcrnrlon=-119,llcrnrlat=22,urcrnrlon=-64,urcrnrlat=49,
        projection='lcc',lat_1=32,lat_2=45,lon_0=-95)

map.drawstates()
map.drawcountries()
map.drawcoastlines()
map.drawrivers(color='blue')
map.shadedrelief() 
#map.drawlakes(color='blue')


# Get the location of each city and plot it
for (city, latitude, longitude) in cities:
    x, y = map(longitude, latitude)
    if city == "Amherst":
        map.plot(x, y, marker='*', color='Black')
    else:
        map.plot(x, y, marker='o',color='Red')
plt.show()
# test