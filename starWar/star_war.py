import argparse
import os

import game_engine
from get_input import _getChUnix as getinp


parser = argparse.ArgumentParser()
parser.add_argument('-r', '--row',
                    help='The row of galaxy. The range of this value is from 5 to 30. The Default value is 16',
                    type=int,
                    default=16)
parser.add_argument('-c', '--column',
                    help='The column of galaxy. The range of this value is from 5 to 30. The Default value is 18',
                    type=int,
                    default=18)
parser.add_argument('-s', '--speed',
                    help='The speed of obstacle. The range of this value is from 0.1 to 1. The Default value is 0.3',
                    type=float, default=0.3)
args = parser.parse_args()


if args.row > 30 or args.row < 5:
    print('the row number should not be greater than 30 and should not be less than 5')
elif args.column > 30 or args.column < 5:
    print('the column number should not be greater than 30 and should not be less than 5')
elif args.speed > 1 or args.speed < 0.1:
    print('the speed should not be greater than 1 and should not be less than 0.1')
else:
    # creating an instance of the game engine
    engine = game_engine.Engine(args.row, args.column, args.speed)

    # general instructions to play the game
    os.system('tput reset')
    print('                ----------------- Star War Begins --------------')
    print('          ----------------- may the force be with you  --------------\n')
    print('Instructions:')
    print('press "a" to move the spaceship to left')
    print('press "d" to move the spaceship to right')
    print('press any key to start the game')
    print('press "q" to quit\n')

    inp = getinp()
    if inp() != 'q':
        engine.run()
    else:
        print('Hail hydra!')
