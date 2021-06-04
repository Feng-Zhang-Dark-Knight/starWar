import signal
import time
from random import randint

from game_classes import Spaceship, Galaxy
from get_input import _getChUnix


class Engine:
    def __init__(self, row, column, speed):
        self.galaxy = Galaxy(row, column)
        self.height = row
        self.width = column
        self.speed = speed
        self.ship = Spaceship(0, self.galaxy)
        self.start = time.time()
        self.getch = _getChUnix()


    def update_scene(self):
        if time.time() - self.start >= self.speed:
            self.start = time.time()

            for r in range(0, self.height)[::-1]:
                if r > 0:
                    self.galaxy.grid[r] = self.galaxy.grid[r - 1].copy()
                    if r == self.height - 1:
                        self._detect_collision()

            self._reset_first_line_of_grid()
            self._add_obstacle_at_first_line_of_grid()

        self.galaxy.grid[self.height - 1][self.ship.position] = '*'


    def run(self):
        def alarmhandler(signum, frame):
            raise TypeError

        def getinp(timeout=0.5):
            signal.signal(signal.SIGALRM, alarmhandler)
            signal.setitimer(signal.ITIMER_REAL, timeout)
            try:
                ch = self.getch()
                signal.alarm(0)
                return ch
            except TypeError:
                pass
            signal.signal(signal.SIGALRM, signal.SIG_IGN)
            return ''

        self._add_obstacle_at_first_line_of_grid()

        while True:
            self.galaxy.render()

            inp = getinp()

            if inp == 'a':
                self.ship.move_left()
            elif inp == 'd':
                self.ship.move_right()
            elif inp == 'q':
                print("Hail hydra!")
                exit()
            else:
                pass

            self.update_scene()

    def _detect_collision(self):
        if self.galaxy.grid[self.height - 1][self.ship.position] == '-':
            print("Game over\n")
            exit()

    def _reset_first_line_of_grid(self):
        """reset the top first line of the obstacle"""
        for i in range(self.width):
            self.galaxy.grid[0][i] = ' '

    def _add_obstacle_at_first_line_of_grid(self):
        """add the obstacle to the top first line of the obstacle"""
        for _ in range(randint(1, int(self.width / 2))):
            self.galaxy.grid[0][randint(0, self.width - 1)] = '-'
