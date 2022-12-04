"""
Run module. This is where the application starts.
"""

from ursina import Ursina


def main() -> None:
    """
    Main function. This is where the application starts.
    """
    ursina = Ursina()

    from src import Game

    game = Game(ursina)
    game.start()


if __name__ == "__main__":
    main()
