"""
Module containing the "Hand" Class.
"""

# TYPING IMPORTS
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..player import Player

# MODULE IMPORTS
from ursina import Entity, Vec3, destroy, invoke

from client.src.game.voxel import Voxel, VoxelTextures


class Hand(Entity):
    """
    Class to represent the hand.
    """

    INITIAL_POSITION = Vec3(0.5, 1, 0.3)
    holding_object: Entity

    def __init__(self, player: Player) -> None:
        """
        Constructor used to initialize some values.
        """
        self._set_entity(player)
        self._set_hand_entities()

    def change_holding_object(self, object: Entity) -> None:
        """
        Method to change the object the hand is holding.

        Parameters
        ----------
        object : Entity
            The object the entity will hold.
        """
        destroy(self.holding_object)
        self.holding_object = object

    def animate(self) -> None:
        """
        Method to animate the hand.

        This method moves the hand to a new position and then move it back.
        """
        self._move_hand_to_active_position()
        invoke(self._move_hand_to_passive_position, delay=0.12)

    def _move_hand_to_active_position(self) -> None:
        """
        Private Method to move the hand to the active position.
        """
        self.position = self.INITIAL_POSITION + Vec3(-0.2, 0, 0.2)

    def _move_hand_to_passive_position(self) -> None:
        """
        Private Method to move the hand to the passive position.
        """
        self.position = self.INITIAL_POSITION

    def _set_entity(self, player: Player) -> None:
        """
        Private Method to set up the hand entity.
        """
        hand_attributes = {
            "parent": player,
            "model": "assets/models/arm/arm.obj",
            "texture": "assets/textures/arm/arm_texture.png",
            "scale": 0.2,
            "position": self.INITIAL_POSITION,
            "rotation": Vec3(140, -10, 0),
        }

        super().__init__(**hand_attributes)

    def _set_hand_entities(self) -> None:
        """
        Private Method to set the hand-related entities.
        """
        voxel_attributes = {
            "parent": self,
            "texture": VoxelTextures.GRASS.value,
            "scale": 0.8,
            "position": self.INITIAL_POSITION + Vec3(-0.4, -0.6, -4.6),
            "rotation": Vec3(200, 0, 0),
        }

        self.holding_object = Voxel(**voxel_attributes)
