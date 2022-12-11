"""
Module containing the "PlayerCommandHandler" Class.
"""
# TYPING IMPORTS
from __future__ import annotations
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from .player import Player

# MODULE IMPORTS
from ursina import Audio, Entity, Vec3, distance, mouse

from src.game.voxel import Voxel, VoxelTextures


class PlayerCommandHandler:
    """
    Class containing functionalities to handle the player commands.
    """

    _player: Player

    def __init__(self, player: Player) -> None:
        """
        Constructor used to initialize some values.
        """
        self._player = player

    def handle_left_mouse_click(self) -> None:
        """
        Method to handle when the player left clicks ("left mouse down").
        """
        hovered_entity: Entity = mouse.hovered_entity

        self._player.hand.animate()
        self._play_punch_sound()

        if not hovered_entity:
            return

        entity_out_of_range = self._is_entity_out_of_range(hovered_entity)

        if entity_out_of_range:
            return

        if hasattr(hovered_entity, "handle_click"):
            hovered_entity.handle_click()

    def handle_right_mouse_click(self) -> None:
        """
        Method to hande when the player right clicks ("right mouse down").
        """
        hovered_entity: Optional[Entity] = mouse.hovered_entity

        self._player.hand.animate()

        if not hovered_entity:
            return

        voxel_position = hovered_entity.position + mouse.normal

        voxel_attributes = {
            "position": voxel_position,
            "texture": self._player.hand.holding_object.texture,
        }

        Voxel(**voxel_attributes)

    def handle_number_1(self) -> None:
        """
        Method to handle when the player type "1".
        """
        voxel = self._create_ui_voxel(VoxelTextures.GRASS)
        self._player.hand.change_holding_object(voxel)

    def handle_number_2(self) -> None:
        """
        Method to handle when the player type "2".
        """
        voxel = self._create_ui_voxel(VoxelTextures.DIRT)
        self._player.hand.change_holding_object(voxel)

    def handle_number_3(self) -> None:
        """
        Method to handle when the player type "3".
        """
        voxel = self._create_ui_voxel(VoxelTextures.STONE)
        self._player.hand.change_holding_object(voxel)

    def handle_number_4(self) -> None:
        """
        Method to handle when the player type "4".
        """
        voxel = self._create_ui_voxel(VoxelTextures.BRICK)
        self._player.hand.change_holding_object(voxel)

    def _is_entity_out_of_range(self, entity: Entity) -> bool:
        """
        Private Method to check whether the entity received as argument
        is out of the player's range or not.

        Parameters
        ----------
        entity : Entity
            The entity to compare its position

        Returns
        --------
        bool
            - True if the entity is out of range (too far);
            - False otherwise.
        """
        return distance(self._player, entity) > self._player.RANGE

    def _create_ui_voxel(self, texture: VoxelTextures) -> Voxel:
        """
        Private Method to create an UI voxel to be displayed in the hand.

        # TODO: REFACTOR THIS METHOD!
        """
        voxel_attributes = {
            "parent": self._player.hand,
            "texture": texture.value,
            "scale": 0.8,
            "position": self._player.hand.INITIAL_POSITION + Vec3(-0.4, -0.6, -4.6),
            "rotation": Vec3(200, 0, 0),
        }

        voxel = Voxel(**voxel_attributes)

        return voxel

    def _play_punch_sound(self) -> None:
        """
        Private Method to play the punch sound.
        """
        punch_sound = Audio("assets/sounds/punch_sound.wav", loop=False, autoplay=False)
        punch_sound.play()
