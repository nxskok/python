import math

def distance(x0, y0, x1, y1): 
  ''' calculate the distance between (x0, y0) and (x1, y1) '''
  return math.sqrt((x1-x0) ** 2 + (y1 - y0) ** 2)  

print(distance(1,2,3,4))
