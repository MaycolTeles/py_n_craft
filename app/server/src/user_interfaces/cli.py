"""
Module containing the "CLI" Class.
"""

# TYPING IMPORTS
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.server.src.servers.game_server import GameServer


class CLI:
    """"""

    """
    Class to represent a "CLI" (Command Line Interface) user interface.
    """

    def __init__(self, game_server: GameServer) -> None:
        """"""
        self._game_server = game_server
        self._show_intro()

    def run(self) -> None:
        """
        Method to execute the user interface.
        """
        self._show_menu()

    def _show_intro(self) -> None:
        """"""
        print("This is the terminal to run some commands.")
        print('If you want to check all the available commands, just type "help".')

    def _show_menu(self) -> None:
        """"""
        self.AVAILABE_COMMANDS = {
            "help": self._show_help,
            "q": self._shut_down,
            "quit": self._shut_down,
        }

        user_option = self._get_user_option()
        menu_function = self.AVAILABE_COMMANDS.get(user_option, self._no_valid_option)

        menu_function()

    def _show_help(self) -> None:
        """"""
        self._show_available_commands()

    def _shut_down(self) -> None:
        """"""
        print("Shutting down the server. Bye.")

        self._game_server.is_running = False
        self._game_server.shut_down()

    def _no_valid_option(self) -> None:
        """"""
        print("Sorry, but that's not a valid option. Please, try again.")
        print('Type "help" to see all available commands.')

    def _show_available_commands(self) -> None:
        """"""
        print("AVAILABLE SERVER COMMANDS:")

        for command in self.AVAILABE_COMMANDS:
            print(f"-> {command}")

        print()

    def _get_user_option(self) -> str:
        option = input(">> ")
        print()
        return option
