class Cell:
    def __init__(self, x1, y1, x2, y2, win):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        self.__win = win
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False

    def draw(self):
        canvas = self.__win.get_canvas()
        if self.has_left_wall:
            canvas.create_line(self.__x1, self.__y1, self.__x1, self.__y2)
        if self.has_right_wall:
            canvas.create_line(self.__x2, self.__y1, self.__x2, self.__y2)
        if self.has_top_wall:
            canvas.create_line(self.__x1, self.__y1, self.__x2, self.__y1)
        if self.has_bottom_wall:
            canvas.create_line(self.__x1, self.__y2, self.__x2, self.__y2)

    def delete_walls(self):
        canvas = self.__win.get_canvas()
        bg_color = canvas.cget("bg")
        if not self.has_left_wall:
            canvas.create_line(self.__x1, self.__y1, self.__x1, self.__y2, fill=bg_color)
        if not self.has_right_wall:
            canvas.create_line(self.__x2, self.__y1, self.__x2, self.__y2, fill=bg_color)
        if not self.has_top_wall:
            canvas.create_line(self.__x1, self.__y1, self.__x2, self.__y1, fill=bg_color)
        if not self.has_bottom_wall:
            canvas.create_line(self.__x1, self.__y2, self.__x2, self.__y2, fill=bg_color)

    def cell_draw(self, to_cell, undo=False):
        color = "red" if not undo else "gray"
        canvas = self.__win.get_canvas()

        ax1 = self.__x1 if self.__x1 < self.__x2 else self.__x2
        ay1 = self.__y1 if self.__y1 < self.__y2 else self.__y2
        ax2 = self.__x2 if self.__x1 < self.__x2 else self.__x1
        ay2 = self.__y2 if self.__y1 < self.__y2 else self.__y1

        start_x = ax1 + ((ax2 - ax1) / 2)
        start_y = ay1 + ((ay2 - ay1) / 2)

        bx1 = to_cell.__x1 if to_cell.__x1 < to_cell.__x2 else to_cell.__x2
        by1 = to_cell.__y1 if to_cell.__y1 < to_cell.__y2 else to_cell.__y2
        bx2 = to_cell.__x2 if to_cell.__x1 < to_cell.__x2 else to_cell.__x1
        by2 = to_cell.__y2 if to_cell.__y1 < to_cell.__y2 else to_cell.__y1

        end_x = bx1 + ((bx2 - bx1) / 2)
        end_y = by1 + ((by2 - by1) / 2)

        canvas.create_line(start_x, start_y, end_x, end_y, fill=color)
