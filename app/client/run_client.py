"""
Run module. This is where the application starts.
"""

# import sys

from .src import GameClient
from ursina import Ursina


ursina = Ursina()


def main() -> None:
    """
    Main function. This is where the application starts.
    """
    # from .src import Game

    # window_position_x = sys.argv[1]
    # window_position_y = sys.argv[2]

    # position = (window_position_x, window_position_y)

    # game = Game(ursina, position=position)

    client = GameClient()
    client.start()


if __name__ == "__main__":
    main()
