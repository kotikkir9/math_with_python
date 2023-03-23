from linear_regression import least_squares
from objects import Point2D

points = [Point2D(1,2), Point2D(2,4), Point2D(3,5), Point2D(4,4), Point2D(5,5)]

def test_least_squares_1():
    result = least_squares(points)
    assert result.intercept == 2.2
    assert result.slope == 0.6
    assert result.equation_string() == 'y = 2.2 + 0.6x'

def test_least_squares_2():
    points.extend([Point2D(6,4), Point2D(7,8)])
    result = least_squares(points)
    assert round(result.intercept, 3) == 2
    assert round(result.slope, 3) == 0.643
    assert result.equation_string() == 'y = 2.0 + 0.643x'

def test_least_squares_3():
    points.extend([Point2D(4,1), Point2D(10,8)])
    result = least_squares(points)
    assert round(result.intercept, 3) == 1.548
    assert round(result.slope, 3) == 0.644
    assert result.equation_string() == 'y = 1.548 + 0.644x'
