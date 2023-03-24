class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Linear_Regression:
    def __init__(self):
        self.intercept = 0 
        self.slope = 0
        self.r_squared = 0
        self.mean_square_error = 0

    def equation_string(self) -> str:
        return f'y = {round(self.intercept, 3)} + {round(self.slope, 3)}x'
    
    def to_string(self) -> str:
        return f'Y-intercept: {self.intercept}\nSlope: {self.slope}\nR squared: {self.r_squared}\nMean Square Error: {self.mean_square_error}\nEquation: {self.equation_string()}'