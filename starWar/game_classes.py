import os


class Galaxy:

    def __init__(self, row, column):
        self.grid = [[' ' for _ in range(column)] for _ in range(row)]

    def print_boundary(self):
        boundary_str = '         '
        cnt = len(self.grid[0]) + 1
        for i in range(cnt):
            boundary_str = boundary_str + '-'
        print(boundary_str)

    def print_row(self, row):
        """print current row.

        Args:
            row: current row
        """
        row_str = '         |'
        for i in range(len(row)):
            row_str = row_str + row[i]
        row_str = row_str + '|'
        print(row_str)

    def render(self):
        """render the obstacle grid"""
        os.system('tput reset')
        self.print_boundary()
        for i in range(len(self.grid)):
            self.print_row(self.grid[i])
        self.print_boundary()
        print('\n\n')


class Spaceship:

    def __init__(self, position, galaxy):
        self.position = position
        self.galaxy = galaxy
        self.galaxy.grid[-1][0] = '*'

    def move_left(self):
        if self.position > 0:
            if self.galaxy.grid[-1][self.position - 1] == '-':
                print("Game over\n")
                exit()
            self.galaxy.grid[-1][self.position] = ' '
            self.galaxy.grid[-1][self.position - 1] = '*'
            self.position = self.position - 1
            self.galaxy.render()

    def move_right(self):
        if self.position < len(self.galaxy.grid[0]) - 1:
            if self.galaxy.grid[-1][self.position + 1] == '-':
                print("Game over\n")
                exit()
            self.galaxy.grid[-1][self.position] = ' '
            self.galaxy.grid[-1][self.position + 1] = '*'
            self.position = self.position + 1
            self.galaxy.render()
