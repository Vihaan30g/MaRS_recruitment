
# medium dose: Q5
# Movement of 3D objects in space and problem with euler system was understood in depth.

import math

def euler_to_quaternion(roll, pitch, yaw):

    # Convert angles from deg to rad
    roll = math.radians(roll)
    pitch = math.radians(pitch)
    yaw = math.radians(yaw)

    # Half angles
    cr = math.cos(roll / 2)
    sr = math.sin(roll / 2)
    cp = math.cos(pitch / 2)
    sp = math.sin(pitch / 2)
    cy = math.cos(yaw / 2)
    sy = math.sin(yaw / 2)

    # Calculating quaternion components, formulae taken from web sourses
    w = cr * cp * cy + sr * sp * sy
    x = sr * cp * cy - cr * sp * sy
    y = cr * sp * cy + sr * cp * sy
    z = cr * cp * sy - sr * sp * cy

    return (w, x, y, z)

# Sample input: Euler angles (Roll=30 deg, Pitch=45 deg, Yaw=60 deg)
q = euler_to_quaternion(30, 45, 60)
print("Quaternion: ", q)
