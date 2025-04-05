# Medium Dose Q1

import math
'''
Z coordinate => depth in what rover sees ( -z is forward )
New reference frame = rover's center top
'''
# Transforming: marker coordinates from the camera's frame to the rover's center frame.
def transform(cam_coord):
    x, y, z = cam_coord

    # Since rover center is behind the camera, marker is 55 farther in -z direction from center
    z_new = z - 55

    return (x, y, z_new)  # coords w.r.t. reference frame

# Calculates distance of a coordinate from origin(0,0,0)
def calc_dist(coord):
    x, y, z = coord
    return math.sqrt(x**2 + y**2 + z**2)



# Sample input:
camera_coords = (10, -5, -60)  # Marker seen at this position by camera

# Transform to rover center frame
rover_coords = transform(camera_coords)

# Calculating distances
distance_from_camera = calc_dist(camera_coords)
distance_from_rover_center = calc_dist(rover_coords)

# Output
print("Marker in Camera Frame: ", camera_coords)
print("Marker in Rover's center Frame : ", rover_coords)
print(f"Distance from Camera     : {distance_from_camera: } cm")
print(f"Distance from Rover Center: {distance_from_rover_center: } cm")
