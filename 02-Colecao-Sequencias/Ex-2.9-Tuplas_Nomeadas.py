from collections import namedtuple
City = namedtuple('City', 'name country population coordinates')
Tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(Tokyo)
print(Tokyo.population)
print(Tokyo.coordinates)
print(Tokyo[1])