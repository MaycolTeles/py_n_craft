"""
Module containing the "Game" Class.
"""

from ursina import Ursina, EditorCamera, Entity, Vec3, application, scene

from src.player import Player
from src.world import World
from src.world.constants import WORLD_NEGATIVE_Y_SIZE


class Game(Entity):
    """
    Class to represent the game.
    """

    def __init__(self, ursina: Ursina) -> None:
        """
        Constructor used to initialize some values.
        """
        self._ursina = ursina

        self._set_constants()
        self._set_entites()
        self._set_entity()

    def input(self, key: str) -> None:
        """
        Method to handle the game inputs.

        This method will be called every time that a key is pressed.

        key : str
            The input key in str format.
        """
        if key == "escape":
            quit()

    def update(self) -> None:
        """
        Method to update the game.

        This method will be called on each frame.
        """
        if self._player.y < WORLD_NEGATIVE_Y_SIZE:
            self._kill_player()

    def start(self) -> None:
        """
        Method to start the game.
        """
        self._ursina.run()

    def _kill_player(self) -> None:
        """
        Private Method to kill the player.
        """
        print("PLAYER DIED")
        self._player.die()

    def _set_constants(self) -> None:
        """
        Private Method to set up some game constants.
        """
        pass

    def _set_entity(self) -> None:
        """
        Private Method to set up the game entity.
        """
        game_attributes = {"parent": scene}

        super().__init__(**game_attributes)

    def _set_entites(self) -> None:
        """
        Private Method to set up the game-related entites.
        """
        self._world = World()
        self._player = Player()
        self._editor_camera = EditorCamera(enabled=False, ignore_paused=True)
        self._pause_handler = Entity(ignore_paused=True, input=self._pause_game)

    def _pause_game(self, key: str) -> None:
        """
        Private Method to pause the game.

        The game will be paused/unpaused if the key "tab" is pressed.
        """
        if key != "tab":
            return

        application.paused = not application.paused
        self._editor_camera.enabled = not self._editor_camera.enabled
        self._editor_camera.position = self._player.position + Vec3(0, 2, 0)
        self._player.camera_pivot.enabled = not self._player.camera_pivot.enabled
