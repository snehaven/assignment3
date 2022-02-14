#  File: Geometry.py

#  Description: Using input from a file, the application will determine where shapes are inside other shapes.

#  Student Name: Sneha Venkatesan

#  Student UT EID: sv23377

#  Partner Name: Liyan Deng

#  Partner UT EID: ld26995

#  Course Name: CS 313E

#  Unique Number: 51130

#  Date Created: 2-13-2022

#  Date Last Modified:

import math
import sys

class Point (object):
  # constructor with default values
  def __init__ (self, x, y, z):
      self.x = x
      self.y = y
      self.z = z

  # create a string representation of a Point
  # returns a string of the form (x, y, z)
  def __str__ (self):
      print("(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")")

  # get distance to another Point object
  # other is a Point object
  # returns the distance as a floating point number
  def distance (self, other):
      return (sqrt((self.x-other.x ** 2) + (self.y-other.y ** 2) + (self.z-other.z ** 2)))

  # test for equality between two points
  # other is a Point object
  # returns a Boolean
  def __eq__ (self, other):
      tol = 10e-6
      return (distance(self, other)  < tol)


class Sphere (object):
  # constructor with default values
  def __init__ (self, x, y, z, radius):
      self.x = x
      self.y = y
      self.z = z
      self.radius = radius


  # returns string representation of a Sphere of the form:
  # Center: (x, y, z), Radius: value
  def __str__ (self):
      print("Center: (" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ") Radius: " + str(self.radius))


  # compute surface area of Sphere
  # returns a floating point number
  def area (self):
      return (4)*math.pi*(self.radius ** 2)

  # compute volume of a Sphere
  # returns a floating point number
  def volume (self):
      return (4/3)*math.pi*(self.radius ** 3)

  # determines if a Point is strictly inside the Sphere
  # p is Point object
  # returns a Boolean
  def is_inside_point (self, p):
      return (p.distance(self) < self.radius)

  # determine distance between centers of two spheres
  def origin_distance (self, other):
      return (sqrt(((self.x-other.x) ** 2) + ((self.y-other.y) ** 2) + ((self.z-other.z) ** 2)))

  # determine if another Sphere is strictly inside this Sphere
  # other is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, other):
      return other.radius < (self.radius - origin_distance(other))

  # determine if a Cube is strictly inside this Sphere
  # determine if the eight corners of the Cube are strictly
  # inside the Sphere
  # a_cube is a Cube object
  # returns a Boolean
  def is_inside_cube (self, a_cube):
      side = a_cube.side/2
      point_1 = Point(a_cube.x - , a_cube.y + side, (a_cube.z - side))
      point_2 = Point(a_cube.x - side , a_cube.y - side, (a_cube.z - side))
      point_3 = Point(a_cube.x + side, a_cube.y - side, (a_cube.z - side))
      point_4 = Point(a_cube.x + , a_cube.y + side, (a_cube.z - side))
      point_5 = Point(a_cube.x - , a_cube.y + side, (a_cube.z + side))
      point_6 = Point(a_cube.x - side , a_cube.y - side, (a_cube.z + side))
      point_7 = Point(a_cube.x + side, a_cube.y - side, (a_cube.z + side))
      point_8 = Point(a_cube.x + , a_cube.y + side, (a_cube.z + side))
      if (!self.is_inside_point(point_1)):
          return False
      if (!self.is_inside_point(point_2)):
          return False
      if (!self.is_inside_point(point_3)):
          return False
      if (!self.is_inside_point(point_4)):
          return False
      if (!self.is_inside_point(point_5)):
          return False
      if (!self.is_inside_point(point_6)):
          return False
      if (!self.is_inside_point(point_7)):
          return False
      if (!self.is_inside_point(point_8)):
          return False

      return True

  # determine if a Cylinder is strictly inside this Sphere
  # a_cyl is a Cylinder object
  # returns a Boolean
  def is_inside_cyl (self, a_cyl):
      if (a_cyl.height > self.radius ** 2):
          return False

      distance = sqrt(((self.x-a_cyl.x) ** 2) + ((self.y-a_cyl.y) ** 2))
      radius_top = sqrt(self.radius ** 2 - (a_cyl.height/2 + a_cyl.z - self.z) ** 2)
      radius_bottom = sqrt(self.radius ** 2 - (a_cyl.height/2 - a_cyl.z - self.z) ** 2)

      return (radius_top > (distance + a_cyl.radius)) & (radius_bottom > (distance + a_cyl.radius))

  # determine if another Sphere intersects this Sphere
  # other is a Sphere object
  # two spheres intersect if they are not strictly inside
  # or not strictly outside each other
  # returns a Boolean
  def does_intersect_sphere (self, other):
      return origin_distance(other) < (self.radius + other.radius)

  # determine if a Cube intersects this Sphere
  # the Cube and Sphere intersect if they are not
  # strictly inside or not strictly outside the other
  # a_cube is a Cube object
  # returns a Boolean
  def does_intersect_cube (self, a_cube):
      return origin_distance(other) < (self.radius + other.side/2)

  # return the largest Cube object that is circumscribed
  # by this Sphere
  # all eight corners of the Cube are on the Sphere
  # returns a Cube object
  def circumscribe_cube (self):
      return Cube(self.x, self.y, self.z, ((self.radius*2)/sqrt(3)))

class Cube (object):
  # Cube is defined by its center (which is a Point object)
  # and side. The faces of the Cube are parallel to x-y, y-z,
  # and x-z planes.
  def __init__ (self, x = 0, y = 0, z = 0, side = 1):

  # string representation of a Cube of the form:
  # Center: (x, y, z), Side: value
  def __str__ (self):

  # compute the total surface area of Cube (all 6 sides)
  # returns a floating point number
  def area (self):

  # compute volume of a Cube
  # returns a floating point number
  def volume (self):

  # determines if a Point is strictly inside this Cube
  # p is a point object
  # returns a Boolean
  def is_inside_point (self, p):

  # determine if a Sphere is strictly inside this Cube
  # a_sphere is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, a_sphere):

  # determine if another Cube is strictly inside this Cube
  # other is a Cube object
  # returns a Boolean
  def is_inside_cube (self, other):

  # determine if a Cylinder is strictly inside this Cube
  # a_cyl is a Cylinder object
  # returns a Boolean
  def is_inside_cylinder (self, a_cyl):

  # determine if another Cube intersects this Cube
  # two Cube objects intersect if they are not strictly
  # inside and not strictly outside each other
  # other is a Cube object
  # returns a Boolean
  def does_intersect_cube (self, other):

  # determine the volume of intersection if this Cube
  # intersects with another Cube
  # other is a Cube object
  # returns a floating point number
  def intersection_volume (self, other):

  # return the largest Sphere object that is inscribed
  # by this Cube
  # Sphere object is inside the Cube and the faces of the
  # Cube are tangential planes of the Sphere
  # returns a Sphere object
  def inscribe_sphere (self):

class Cylinder (object):
  # Cylinder is defined by its center (which is a Point object),
  # radius and height. The main axis of the Cylinder is along the
  # z-axis and height is measured along this axis
  def __init__ (self, x = 0, y = 0, z = 0, radius = 1, height = 1):

  # returns a string representation of a Cylinder of the form:
  # Center: (x, y, z), Radius: value, Height: value
  def __str__ (self):

  # compute surface area of Cylinder
  # returns a floating point number
  def area (self):

  # compute volume of a Cylinder
  # returns a floating point number
  def volume (self):

  # determine if a Point is strictly inside this Cylinder
  # p is a Point object
  # returns a Boolean
  def is_inside_point (self, p):

  # determine if a Sphere is strictly inside this Cylinder
  # a_sphere is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, a_sphere):

  # determine if a Cube is strictly inside this Cylinder
  # determine if all eight corners of the Cube are inside
  # the Cylinder
  # a_cube is a Cube object
  # returns a Boolean
  def is_inside_cube (self, a_cube):

  # determine if another Cylinder is strictly inside this Cylinder
  # other is Cylinder object
  # returns a Boolean
  def is_inside_cylinder (self, other):

  # determine if another Cylinder intersects this Cylinder
  # two Cylinder object intersect if they are not strictly
  # inside and not strictly outside each other
  # other is a Cylinder object
  # returns a Boolean
  def does_intersect_cylinder (self, other):

def main():
  # read data from standard input
  data = sys.stdin.read()
  data_list = data.split("\n")

  # read the coordinates of the first Point p
  p = data_list[0].split()

  # create a Point object
  p = Point(float(p[0]), float(p[1]), float(p[2])

  # read the coordinates of the second Point q
  q = data_list[1].split()

  # create a Point object
  p = Point(float(q[0]), float(q[1]), float(q[2]))

  # read the coordinates of the center and radius of sphereA
  sphereA = data_list[2].split()

  # create a Sphere object
  sphereA = Sphere(float(sphereA[0]), float(sphereA[1]), float(sphereA[2]), float(sphereA[3]))

  # read the coordinates of the center and radius of sphereB
  sphereB = data_list[3].split()

  # create a Sphere object
  sphereB = Sphere(float(sphereB[0]), float(sphereB[1]), float(sphereB[2]), float(sphereB[3]))

  # read the coordinates of the center and side of cubeA
  cubeA = data_list[4].split()

  # create a Cube object
  cubeA = Cube(float(cubeA[0]), float(cubeA[1]), float(cubeA[2]), float(cubeA[3]))

  # read the coordinates of the center and side of cubeB
  cubeB = data_list[5].split()

  # create a Cube object
  cubeB = Cube(float(cubeB[0]), float(cubeB[1]), float(cubeB[2]), float(cubeB[3]))

  # read the coordinates of the center, radius and height of cylA
  cylA = data_list[6].split()

  # create a Cylinder object
  cylA = Cylinder(float(cylA[0]), float(cylA[1]), float(cylA[2]), float(cylA[3]))

  # read the coordinates of the center, radius and height of cylB
  cylB = data_list[6].split()
  # create a Cylinder object
  cylB = Cylinder(float(cylB[0]), float(cylB[1]), float(cylB[2]), float(cylB[3]))

  #origin Point
  origin = Point(0,0,0)

  # print if the distance of p from the origin is greater
  # than the distance of q from the origin
  if (p.distance(origin) > q.distance(origin)):
      print("Distance of Point p from the origin is greater than the distance of Point q from the origin")
   else:
      print("Distance of Point p from the origin is not greater than the distance of Point q from the origin")

  # print if Point p is inside sphereA
  if (sphereA.is_inside_point(p)):
      print("Point p is inside sphereA")
  else:
      print("Point p is not inside sphereA")

  # print if sphereB is inside sphereA
  if (sphereA.is_inside_sphere(sphereB)):
      print("sphereB is inside sphereA")
   else:
      print("sphereB is not inside sphereA")

  # print if cubeA is inside sphereA
  if (sphereA.is_inside_cube(cubeA)):
      print("cubeA is inside sphereA")
  else:
      print("cubeA is not inside sphereA")

  # print if cylA is inside sphereA
  if (sphereA.is_inside_cyl(cylA)):
      print("cylA is inside sphereA")
  else:
      print("cylA is not inside sphereA")

  # print if sphereA intersects with sphereB
  if (sphereA.does_intersect_sphere(sphereB)):
      print("sphereA does intersect sphereB")
  else:
      print("sphereA does not intersect sphereB")

  # print if cubeB intersects with sphereB
  if (sphereB.does_intersect_cube(cubeB)):
      print("cubeB does intersect sphereB")
  else:
      print("cubeB does not intersect sphereB")

  # print if the volume of the largest Cube that is circumscribed
  # by sphereA is greater than the volume of cylA
  if (sphereA.circumscribe_cube().volume() > cylA.volume()):
      print("Volume of the largest Cube that is circumscribed by sphereA is greater than the volume of cylA")
  else:
      print("Volume of the largest Cube that is circumscribed by sphereA is not greater than the volume of cylA")

  # print if Point p is inside cubeA
  if (cubeA.is_inside_point(p)):
      print("Point p is inside cubeA")
  else:
      print("Point p is not inside cubeA")

  # print if sphereA is inside cubeA
  if (cubeA.is_inside_sphere(sphereA)):
      print("sphereA is inside cubeA")
  else:
      print("sphereA is not inside cubeA")

  # print if cubeB is inside cubeA
  if (cubeA.is_inside_cube(cubeB)):
      print("cubeB is inside cubeA")
  else:
      print("cubeB is not inside cubeA")

  # print if cylA is inside cubeA
  if (cubeA.is_inside_cyl(cylA)):
      print("cylA is inside cubeA")
  else:
      print("cylA is not inside cubeA")

  # print if cubeA intersects with cubeB
  if (cubeA.does_intersect_cube(cubeB)):
      print("cubeA does intersect cubeB")
  else:
      print("cubeA does not intersect cubeB")

  # print if the intersection volume of cubeA and cubeB
  # is greater than the volume of sphereA
  if (cubeA.intersection_volume(cubeB) > sphereA.volume()):
      print("Intersection volume of cubeA and cubeB is greater than the volume of sphereA")
  else:
      print("Intersection volume of cubeA and cubeB is not greater than the volume of sphereA")

  # print if the surface area of the largest Sphere object inscribed
  # by cubeA is greater than the surface area of cylA
  if (cubeA.inscribe_sphere().area() > cylA.area()):
      print("Surface area of the largest Sphere object inscribed by cubeA is greater than the surface area of cylA")
  else:
      print("Surface area of the largest Sphere object inscribed by cubeA is not greater than the surface area of cylA")

  # print if Point p is inside cylA
  if (cylA.is_inside_point(p)):
      print("Point p is inside cylA")
  else:
      print("Point p is not inside cylA")

  # print if sphereA is inside cylA
  if (cylA.is_inside_sphere(sphereA)):
      print("sphereA is inside cylA")
  else:
      print("sphereA is not inside cylA")

  # print if cubeA is inside cylA
  if (cylA.is_inside_cube(cubeA)):
      print("cubeA is inside cylA")
  else:
      print("cubeA is not inside cylA")

  # print if cylB is inside cylA
  if (cylA.is_inside_cyl(cylB)):
      print("cylB is inside cylA")
  else:
      print("cylB is not inside cylA")

  # print if cylB intersects with cylA
  if (cylA.does_intersect_cylinder(cylB)):
      print("cylB does intersect cylA")
  else:
      print("cylB does not intersect cylA")

if __name__ == "__main__":
  main()
