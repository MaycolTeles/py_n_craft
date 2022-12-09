"""
Run module. This is where the application starts.
"""

from ursina import Ursina

ursina = Ursina()


def main() -> None:
    """
    Main function. This is where the application starts.
    """
    from src import Game, GameClient

    client = GameClient()

    game = Game(ursina, client)
    game.start()


if __name__ == "__main__":
    main()
