"""
Run module. This is where the application starts.
"""

from src import game_server


def main() -> None:
    """
    Main function. This is where the application starts.
    """
    game_server.start()


if __name__ == "__main__":
    main()
