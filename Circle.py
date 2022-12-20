import math
r=float(input("enter radius of circle:"))
def area(r):
    area=2*math.pi*r
    return area
def perimeter(r):
    peri=math.pi*r**2
    return peri
print("area of the circle :",area(r))
print("perimeter of circle is:",perimeter(r) )

