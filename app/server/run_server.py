"""
Run module. This is where the application starts.
"""

from server.src import GameServer


def main() -> None:
    """
    Main function. This is where the application starts.
    """
    game_server = GameServer()
    game_server.start()


if __name__ == "__main__":
    main()
