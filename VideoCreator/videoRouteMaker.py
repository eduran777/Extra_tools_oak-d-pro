import cv2
import folium
from folium.plugins import MarkerCluster
import numpy as np
import csv
import selenium
# Define the size of the video frame and the map
FRAME_WIDTH, FRAME_HEIGHT = 1280, 720
MAP_WIDTH, MAP_HEIGHT = 240, 320
# Load the video
cap = cv2.VideoCapture('/Users/usuario/Documents/Frames/Frames interpolacion/routeClip3fps/Clip6.mp4')

def formatC(cf):
    cf = cf[0:len(cf)-1]
    return float(cf)


# Create a map centered at the first GPS point
#gps_points = [(lat, lon) for lat, lon in zip(latitudes, longitudes)]
mapBog = folium.Map(location=[4.657837499999999,-74.05332609999999],zoom_start=13, width=MAP_WIDTH, height=MAP_HEIGHT)
# Create a marker cluster layer
marker_cluster = MarkerCluster().add_to(mapBog)
# Loop through the video frames and add markers to the map
frame_num = 0

with open('/Users/usuario/Documents/pruebas 03-03-2023/Cordeenadas /Cordenadas intercep /coordenadasIntercept.CSV','r') as csv_table:
    csv_reader = csv.reader(csv_table)
    next(csv_reader)

    rows = list(csv_reader)



while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    print(frame.size)
    print(frame.shape)
    # Get the GPS location of the current frame
    gps_location = [formatC(rows[frame_num][4]),formatC(rows[frame_num][5])]
    # Add a marker to the marker cluster layer
    folium.Marker(location=gps_location, icon=None).add_to(marker_cluster)
    # Convert the map to an image and resize it to fit in the video frame
    print(type(mapBog))
    map_img = mapBog._to_png()
    map_img = cv2.imdecode(np.frombuffer(map_img, np.uint8), cv2.IMREAD_UNCHANGED)
    map_img = cv2.resize(map_img, (MAP_WIDTH, 400))
    # Combine the map and the frame
    combined = np.zeros((FRAME_HEIGHT, FRAME_WIDTH, 4), np.uint8)
    combined[MAP_HEIGHT:FRAME_HEIGHT, 0:MAP_WIDTH] = map_img
    print(combined.shape)

    combined[0:192, 280:FRAME_WIDTH] = frame
    # Display the combined image in a window
    cv2.imshow('Frame with Map', combined)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
    # Increment the frame number
    frame_num += 1
# Release the video and close the window
cap.release()
cv2.destroyAllWindows()
# Save the map as an HTML file
mapBog.save('map.html')
