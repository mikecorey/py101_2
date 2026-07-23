import random

#generates 10 points with random latitudes and longitudes
baseline_center = (30.41731572197938, -86.67136966638938)
random_points = []
for i in range(10):
    lat = baseline_center[0] + random.uniform(-0.1, 0.1)
    lon = baseline_center[1] + random.uniform(-0.1, 0.1)
    random_points.append((lat, lon))


#actual_computation
center_lat = 0
center_lon = 0
for point in random_points:
    center_lat += point[0]
    center_lon += point[1]

center_lat /= len(random_points)
center_lon /= len(random_points)

print(f"Computed center: ({center_lat}, {center_lon})")

# Adding 5 more points around a second center
second_center = (30.417928539667603, -86.65447665011267)
for i in range(10):
    lat = second_center[0] + random.uniform(-0.1, 0.1)
    lon = second_center[1] + random.uniform(-0.1, 0.1)
    random_points.append((lat, lon))



#actual_computation
second_center_lat = 0
second_center_lon = 0
for point in random_points:
    second_center_lat += point[0]
    second_center_lon += point[1]

second_center_lat /= len(random_points)
second_center_lon /= len(random_points)

print(f"second Computed center: ({second_center_lat}, {second_center_lon})")
f = open('compute_lat_long_center.csv', 'w')
f.write('name,lat,lon\n')
for i, point in enumerate(random_points):
    f.write(f'point_{i},{point[0]},{point[1]}\n')
f.write(f'second_computed_center,{second_center_lat},{second_center_lon}\n')
f.write(f'first_computed_center,{center_lat},{center_lon}\n')
