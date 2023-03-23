from objects import Linear_Regression

def least_squares(points) -> Linear_Regression:
    x_total = 0
    y_total = 0
    for i in points:
        x_total += i.x
        y_total += i.y

    x_mean = x_total / len(points)
    y_mean = y_total / len(points)

    x_y_total = 0
    x_pow_total = 0

    for i in points:
        x_pow_total += (i.x - x_mean) ** 2
        x_y_total += (i.x - x_mean) * (i.y - y_mean)

    b1= x_y_total / x_pow_total
    b0 = y_mean - (b1 * x_mean)
    return Linear_Regression(b0, b1)
