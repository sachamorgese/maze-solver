from tkinter import Tk, Canvas


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, width=width, height=height)
        self.__canvas.pack()
        self.__width = width
        self.__height = height
        self.window_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.center_window(self.__width, self.__height)

    def center_window(self, width=300, height=200):
        # get screen width and height
        screen_width = self.__root.winfo_screenwidth()
        screen_height = self.__root.winfo_screenheight()

        # calculate position x and y coordinates
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.__root.geometry('%dx%d+%d+%d' % (width, height, x, y))

    def get_canvas(self):
        return self.__canvas

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.window_running = True
        while self.window_running:
            self.redraw()

    def close(self):
        self.window_running = False
