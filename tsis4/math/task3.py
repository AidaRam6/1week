import math
def polygon_area(sides , length ):
    return ((length / (2 * math.tan(math.pi / sides))) * (sides * length)) /2
s = int(input("s:"))
l = int(input("l:"))
area = polygon_area(s , l)
print(int(area))