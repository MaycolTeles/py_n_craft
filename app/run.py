"""
Run module. This is where the application starts.
"""

import threading

from client import run_client
from server import run_server


def main() -> None:
    """
    Main function. This is where the application starts.
    """
    server_thread = threading.Thread(target=run_server.main)
    client_thread = threading.Thread(target=run_client.main)

    server_thread.start()
    client_thread.start()


if __name__ == "__main__":
    main()
