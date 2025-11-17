#area = math.sqrt(s * (s - a) * (s - b) * (s - c))

###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides
#
import math
def triangle_area(a,b,c):
    s = (a+b+c)/2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    
    return area

wynik = triangle_area(3,5,7)

print(f'The area of ​​a triangle with sides 3,5,7 is {wynik}')
print('The area of ​​a triangle with sides ... is ...')
print('The area of ​​a triangle with sides ... is ...')