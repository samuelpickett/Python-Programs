import folium
import pandas

def color_icon(elev):
    mini = int(min(df["ELEV"]))
    step = int((max(df["ELEV"]) - mini)/3)
    if elev in range(mini, mini + step):
        color="green" 
    elif elev in range(mini + step, mini + step*2):
        color = "orange"
    else:
        color = "red"
    return color

df = pandas.read_csv("Web Mapping\Volcanoes.txt")

map = folium.Map(location = [df["LAT"].mean(), df["LON"].mean()], zoom_start=4)
pop_map = folium.GeoJson(data=open("Web Mapping\pop.json"),style_function=lambda x:{"fillcolor": "green" if x["properties"]["POP2005"]<= 10000000 else "orange" if 10000000<x["properties"]["POP2005"] else "red"}, name="World Population")


for lat, lon, name, elev in zip(df["LAT"], df["LON"], df["NAME"], df["ELEV"]):
    map.add_child(folium.Marker(location=[lat, lon], popup=name, icon=folium.Icon(color=color_icon(elev))))
map.add_child(pop_map)
map.save(outfile="Web Mapping\map.html")