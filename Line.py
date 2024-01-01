class Line:
    def __init__(self, point1, point2, canvas):
        self.__point1 = point1
        self.__point2 = point2
        self.__canvas = canvas

    def draw(self):
        self.__line = self.__canvas.create_line(self.__point1.x, self.__point1.y, self.__point2.x, self.__point2.y, width=2)
