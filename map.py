import folium
map = folium.Map(location=[34.37, -102.77], zoom_start=6, tiles="Mapbox Bright")

map.add_child(folium.Marker(location=[34.2,-102.1], popup="Hi I am Ajay",icon=folium.Icon(color='blue')))

map.save("Map1.html")