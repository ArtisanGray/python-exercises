import math
class circle:
  
  def __init__(self, radius):
    print("Circle Constructor run!")
    self.radius = radius
  def area(self):
   print (math.pi * self.radius**2)
  def perimeter(self):
   print (2*(math.pi * self.radius))
circletwo = circle(3)
circletwo.area()
circletwo.perimeter()
