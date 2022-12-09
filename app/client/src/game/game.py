"""
Module containing the "Game" Class.
"""

from ursina import Ursina, Entity, window

from .player import Player
from .world import World
from src.client import GameClient


class Game(Entity):
    """
    Class to represent the game.
    """

    _game_client: GameClient
    _player: Player
    _world: World

    def __init__(self, ursina: Ursina, game_client: GameClient) -> None:
        """
        Constructor used to initialize some values.
        """
        self._ursina = ursina
        self._game_client = game_client

        self._set_entites()
        self._set_entity()

        window.size = (600, 600)
        window.position = (1600, 0)

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
        self._game_client.client.process_net_events()

    def start(self) -> None:
        """
        Method to start the game.
        """
        self._ursina.run()

    def _set_entity(self) -> None:
        """
        Private Method to set up the game entity.
        """
        super().__init__()

    def _set_entites(self) -> None:
        """
        Private Method to set up the game-related entites.
        """
        self._player = Player()
        self._world = World()
        # self._editor_camera = EditorCamera(enabled=False, ignore_paused=True)
        # self._pause_handler = Entity(ignore_paused=True, input=self._pause_game)

    # def _pause_game(self, key: str) -> None:
    #     """
    #     Private Method to pause the game.

    #     The game will be paused/unpaused if the key "tab" is pressed.
    #     """
    #     if key != "tab":
    #         return

    #     application.paused = not application.paused
    #     self._editor_camera.enabled = not self._editor_camera.enabled
    #     self._editor_camera.position = self._player.position + Vec3(0, 2, 0)
    #     self._player.camera_pivot.enabled = not self._player.camera_pivot.enabled
