from linear_regression import calculate
from objects import Point2D

values = [Point2D(1,2), Point2D(2,4), Point2D(3,5), Point2D(4,4), Point2D(5,5)]

def test_least_squares_1():
    result = calculate(values)
    assert round(result.intercept, 3) == 2.2
    assert round(result.slope, 3) == 0.6
    assert round(result.r_squared, 3) == 0.6
    assert round(result.mean_square_error, 3) == 0.894
    assert result.equation_string() == 'y = 2.2 + 0.6x'

def test_least_squares_2():
    values.extend([Point2D(6,4), Point2D(7,8)])
    result = calculate(values)
    assert round(result.intercept, 3) == 2
    assert round(result.slope, 3) == 0.643
    assert round(result.r_squared, 3) == 0.587
    assert round(result.mean_square_error, 3) == 1.276
    assert result.equation_string() == 'y = 2.0 + 0.643x'

def test_least_squares_3():
    values.extend([Point2D(4,1), Point2D(10,8)])
    result = calculate(values)
    assert round(result.intercept, 3) == 1.548
    assert round(result.slope, 3) == 0.644
    assert round(result.r_squared, 3) == 0.563
    assert round(result.mean_square_error, 3) == 1.661
    assert result.equation_string() == 'y = 1.548 + 0.644x'
