import math
def polygon_area(sides, length):

    area= (sides*0.25)*(length**2) / math.tan(math.pi/sides)
    return area

print polygon_area(7,3)

