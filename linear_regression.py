from objects import Linear_Regression
import math

def calculate(points) -> Linear_Regression:
    lg = Linear_Regression()
    
    x_total = 0
    y_total = 0
    for i in points:
        x_total += i.x
        y_total += i.y

    x_mean = x_total / len(points)
    y_mean = y_total / len(points)

    # Calculate linear regression using least square method
    sum_xxmean_yymean = 0
    sum_x_xmean_square = 0

    for i in points:
        sum_x_xmean_square += (i.x - x_mean) ** 2
        sum_xxmean_yymean += (i.x - x_mean) * (i.y - y_mean)

    lg.slope = sum_xxmean_yymean / sum_x_xmean_square
    lg.intercept = y_mean - (lg.slope * x_mean)

    # Calculate R Squared Using Regression Analysis
    sum_yhat_ymean_square = 0
    sum_y_ymean_square = 0

    for i in points:
        sum_y_ymean_square += (i.y - y_mean) ** 2
        sum_yhat_ymean_square += ((lg.intercept + i.x * lg.slope) - y_mean) ** 2
    
    lg.r_squared = sum_yhat_ymean_square / sum_y_ymean_square

    # Standard Error of the Estimate used in Regression Analysis
    sum_yhat_y_square = 0
    
    for i in points:
        sum_yhat_y_square += ((lg.intercept + i.x * lg.slope) - i.y) ** 2

    lg.mean_square_error = math.sqrt(sum_yhat_y_square / (len(points) - 2))

    return lg
