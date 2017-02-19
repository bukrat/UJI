def turn():

    min_lat_dist = 0.3
    min_left = min(p3dx.distance[0:2])
    min_right = min(p3dx.distance[6:])
    if ( min_right < min_left ):
        while (min(p3dx.distance[3:5]) < max(min_left,0.5) or p3dx.distance[6] < min_lat_dist) :
            p3dx.move(-2,2)
    else:
        while (min(p3dx.distance[3:5]) < max(min_right,0.5) or p3dx.distance[2] < min_lat_dist):
            p3dx.move(2,-2)
    p3dx.stop()