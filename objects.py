class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Linear_Regression:
    def __init__(self, b0, b1):
        self.intercept = b0
        self.slope = b1

    def equation_string(self) -> str:
        return f'y = {round(self.intercept, 3)} + {round(self.slope, 3)}x'