"""
Module containing the "Player" Class.
"""

from typing import Callable

from ursina import Vec3
from ursina.prefabs.first_person_controller import FirstPersonController

from .hand import Hand
from .player_command_handler import PlayerCommandHandler


class Player(FirstPersonController):
    """
    Class to represent the player.
    """

    RANGE = 8
    hand: Hand
    _player_handler: PlayerCommandHandler

    def __init__(self) -> None:
        """
        Constructor used to initialize some values.
        """
        self._player_handler = PlayerCommandHandler(self)
        self._set_entity()
        self._set_player_entites()

    def input(self, key: str) -> None:
        """
        Method to handle the game inputs.

        This method will be called every time that a key is pressed.

        key : str
            The input key in str format.
        """
        super().input(key)

        COMMANDS: dict[str, Callable[[], None]] = {
            "left mouse down": self._player_handler.handle_left_mouse_click,
            "right mouse down": self._player_handler.handle_right_mouse_click,
            "1": self._player_handler.handle_number_1,
            "2": self._player_handler.handle_number_2,
            "3": self._player_handler.handle_number_3,
            "4": self._player_handler.handle_number_4,
        }

        if key in COMMANDS:
            COMMANDS[key]()

    def die(self) -> None:
        """
        Method that must be called when the player dies.
        """
        print("YOU DIED!")
        self.position = Vec3(0, 2, 0)

    def _set_entity(self) -> None:
        """
        Private Method to set up the player entity.
        """
        player_attributes = {"collider": "box"}

        super().__init__(**player_attributes)

    def _set_player_entites(self) -> None:
        """
        Private Method to set up the player-related entities.
        """
        self.hand = Hand(self)
