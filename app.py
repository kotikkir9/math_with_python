from linear_regression import least_squares
from objects import Point2D

points = [Point2D(1,2), Point2D(2,4), Point2D(3,5), Point2D(4,4), Point2D(5,5)]

print(least_squares(points).equation_string())