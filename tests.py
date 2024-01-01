import unittest

from Maze import Maze
from Window import Window

class Tests(unittest.TestCase):
    def test_maze_create_cells_1(self):
        window = Window(800, 800)
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, window)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )

    def test_maze_create_cells_2(self):
        window = Window(800, 800)
        num_cols = 24
        num_rows = 5
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, window)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )

    def test_maze_create_cells_3(self):
        window = Window(800, 800)
        num_cols = 10
        num_rows = 18
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, window)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )

if __name__ == '__main__':
    unittest.main()
