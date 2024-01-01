from Maze import Maze
from Window import Window

def main():
    window = Window(800, 800)

    maze = Maze(0,0, 20, 20, 36, 36, window)
    maze.solve()

    window.wait_for_close()

main()
