import cv2
import folium
from folium.plugins import MarkerCluster
import numpy as np
import csv
from PIL import Image
import os
import selenium
# Define the size of the video frame and the map
FRAME_WIDTH, FRAME_HEIGHT = 1280, 720
MAP_WIDTH, MAP_HEIGHT = 150, 320
tooltip = "Click me!"
# Load the video
cap = cv2.VideoCapture('/Users/usuario/Documents/Frames/Frames interpolacion/routeClip3fps/Clip6.mp4')
#dd
def formatC(cf):
    cf = cf[0:len(cf)-1]
    return float(cf)

#fixfixfix
# Create a map centered at the first GPS point
#gps_points = [(lat, lon) for lat, lon in zip(latitudes, longitudes)]
mapBog = folium.Map(location=[4.657837499999999,-74.05332609999999],zoom_start=12, width=MAP_WIDTH, height=MAP_HEIGHT)
folium.Marker( [4.69059395, -74.03417855000001], popup="<b>Timberline Lodge</b>", tooltip=tooltip).add_to(mapBog)
folium.Marker([4.61560375, -74.0689023], popup="<i>Mt. Hood Meadows</i>", tooltip=tooltip).add_to(mapBog)

# Create a marker cluster layer
marker_cluster = MarkerCluster().add_to(mapBog)
# Loop through the video frames and add markers to the map
frame_num = 0
listMapBog = [mapBog]

with open('/Users/usuario/Documents/pruebas 03-03-2023/Cordeenadas /Cordenadas intercep /coordenadasIntercept.CSV','r') as csv_table:
    csv_reader = csv.reader(csv_table)
    next(csv_reader)

    rows = list(csv_reader)

for i in range (0,len(rows)-3000):
    print(i)
    folium.Marker([formatC(rows[i][4]),-formatC(rows[i][5])], popup="<b>Timberline Lodge</b>", icon=folium.DivIcon(html=f""" <div><svg>
               <circle cx="0" cy="0" r="10" fill="#17d3e6" opacity="1"/>
           </svg></div""")).add_to(mapBog)

   # mapName = 'map'+ str(i)+'.html'

    #listMapBog.append(mapBog)


    #mapBog.save('/Users/usuario/Documents/Pruebas video con mapa /Mapshtml/'+mapName)
    #listMapBog.pop().save('/Users/usuario/Documents/Pruebas video con mapa /MapTest/'+mapName)


while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    #for i in range (0,len(rows)-3000+(frame_num*100)):
    print(i)
    mapBog = folium.Map(location=[4.657837499999999,-74.05332609999999],zoom_start=12, width=MAP_WIDTH, height=MAP_HEIGHT)
    folium.Marker( [4.69059395, -74.03417855000001], popup="<b>Timberline Lodge</b>", tooltip=tooltip).add_to(mapBog)
    folium.Marker([formatC(rows[frame_num][4]),-formatC(rows[frame_num][5])], popup="<b>Timberline Lodge</b>", icon=folium.DivIcon(html=f""" <div style="display: inline-block; width: 0; height: 0; border-top: 5px solid transparent; border-bottom: 5px solid transparent; border-right: 8px solid #0b5394;"></div>""")).add_to(mapBog)
    folium.Marker([formatC(rows[frame_num][4]),-formatC(rows[frame_num][5])], popup="<b>Timberline Lodge</b>", icon=folium.DivIcon(html=f""" <div style="width: 15px; height: 7px; border-radius: 50%; background-color: #17d3e6;"></div>""")).add_to(marker_cluster)

    #path = '/Users/usuario/Documents/Pruebas video con mapa /MapTest/map'+ str(frame_num)+'.html'
    #fileimg = os.open(path,os.O_RDONLY)
    #print(frame.size)
    #print(frame.shape)
    print(frame_num)
    # Get the GPS location of the current frame
    gps_location = [formatC(rows[frame_num][4]),formatC(rows[frame_num][5])]
    # Add a marker to the marker cluster layer

    #folium.Marker(location=gps_location, icon=None).add_to(marker_cluster)
    #folium.Marker([formatC(rows[frame_num][4]),-formatC(rows[frame_num][5])], popup="<b>Timberline Lodge</b>", icon=folium.DivIcon(html=f""" <div><svg>
               #<circle cx="0" cy="0" r="30" fill="#69b3a2" opacity="1"/>
            #</svg></div""")).add_to(mapBog)









    # Convert the map to an image and resize it to fit in the video frame
    #print(type(mapBog))

    map_img = mapBog._to_png()
    map_img = cv2.imdecode(np.frombuffer(map_img, np.uint8), cv2.IMREAD_UNCHANGED)
    map_img = cv2.resize(map_img, (MAP_WIDTH, 400))

    # Combine the map and the frame
    combined = np.zeros((FRAME_HEIGHT, FRAME_WIDTH-630, 4), np.uint8)

    #print(combined.shape)

    combined[320:720, 0:640,0:3] = frame
    combined[(MAP_HEIGHT):(FRAME_HEIGHT), 0:MAP_WIDTH] = map_img



    # Display the combined image in a window
    cv2.imshow('Frame with Map', combined)
    print(combined.__class__)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
    # Increment the frame number
    MarkerCluster().add_to(mapBog)
    frame_num += 1
# Release the video and close the window
cap.release()
cv2.destroyAllWindows()
# Save the map as an HTML file
mapBog.save('map.html')
