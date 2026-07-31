import math

def manhattan(a,b):
    return sum(abs(x  - y) for x, y in zip(a, b))

def euclidean(a, b):
    d_x = b[0] - a[0]
    d_y = b[1] - a[1]

    distance = math.sqrt(d_x**2 + d_y**2)
    return distance