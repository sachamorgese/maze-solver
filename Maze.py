import random

from Cell import Cell
from Window import Window
import time

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win: Window,
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__cells = []
        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0, 0)
        self.__reset_cells_visited()
    def __create_cells(self):
        for col_i in range(self.__num_cols):
            col = []
            for row in range(self.__num_rows):
                cur_y = row * self.__cell_size_y + self.__cell_size_y
                cur_x = col_i * self.__cell_size_x + self.__cell_size_x

                cell = Cell(cur_x, cur_y, cur_x + self.__cell_size_x, cur_y + self.__cell_size_y, self.__win)
                col.append(cell)
            self.__cells.append(col)

        for col_i in range(len(self.__cells)):
            for row_i in range(len(self.__cells[col_i])):
                self.__draw_cells(col_i, row_i)
    def __draw_cells(self, col_i: int, row_i: int):
        cell: Cell = self.__cells[col_i][row_i]
        cell.draw()
        self.__animate()

    def __animate(self):
        self.__win.redraw()

    def __break_entrance_and_exit(self):
        first_cell: Cell = self.__cells[0][0]
        first_cell.has_top_wall = False
        first_cell.delete_walls()
        last_cell = self.__cells[-1][-1]
        last_cell.has_bottom_wall = False
        last_cell.delete_walls()

    def __break_walls_r(self, col_i: int, row_i: int):
        current_cell = self.__cells[col_i][row_i]
        current_cell.visited = True

        while True:
            to_visit = []

            if col_i > 0 and not self.__cells[col_i - 1][row_i].visited:
                to_visit.append((col_i - 1, row_i))
            if col_i < self.__num_cols - 1 and not self.__cells[col_i + 1][row_i].visited:
                to_visit.append((col_i + 1, row_i))
            if row_i > 0 and not self.__cells[col_i][row_i - 1].visited:
                to_visit.append((col_i, row_i - 1))
            if row_i < self.__num_cols - 1 and not self.__cells[col_i][row_i + 1].visited:
                to_visit.append((col_i, row_i + 1))

            if len(to_visit) == 0:
                current_cell.draw()
                return

            random_choice = random.choice(to_visit)

            adjacent_cell = self.__cells[random_choice[0]][random_choice[1]]

            if random_choice[0] > col_i:
                current_cell.has_right_wall = False
                adjacent_cell.has_left_wall = False
            elif random_choice[0] < col_i:
                current_cell.has_left_wall = False
                adjacent_cell.has_right_wall = False
            elif random_choice[1] > row_i:
                current_cell.has_bottom_wall = False
                adjacent_cell.has_top_wall = False
            elif random_choice[1] < row_i:
                current_cell.has_top_wall = False
                adjacent_cell.has_bottom_wall = False

            current_cell.delete_walls()

            self.__animate()

            self.__break_walls_r(random_choice[0], random_choice[1])

    def __reset_cells_visited(self):
        for col in self.__cells:
            for cell in col:
                cell.visited = False

    def solve(self):
        self.__solve_r(0, 0)

    solved = False
    def __solve_r(self, col_i,  row_i):
        current_cell: Cell = self.__cells[col_i][row_i]
        current_cell.visited = True
        if self.__cells[col_i][row_i] == self.__cells[-1][-1]:
            self.solved = True
            return True

        while True:
            if self.solved:
                return True

            to_visit = []

            if not current_cell.has_top_wall and not self.__cells[col_i][row_i - 1].visited and col_i != 0 != row_i:
                to_visit.append((col_i, row_i - 1))
            if not current_cell.has_bottom_wall and not self.__cells[col_i][row_i + 1].visited:
                to_visit.append((col_i, row_i + 1))
            if not current_cell.has_left_wall and not self.__cells[col_i - 1][row_i].visited:
                to_visit.append((col_i - 1, row_i))
            if not current_cell.has_right_wall and not self.__cells[col_i + 1][row_i].visited:
                to_visit.append((col_i + 1, row_i))

            if not to_visit:
                return False

            choice = random.choice(to_visit)
            go_to_cell = self.__cells[choice[0]][choice[1]]
            current_cell.cell_draw(go_to_cell)

            self.__animate()

            found = self.__solve_r(choice[0], choice[1])

            if not found:
                current_cell.cell_draw(go_to_cell, True)
                self.__animate()
