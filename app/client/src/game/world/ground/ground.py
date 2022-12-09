"""
Module containing the "Ground" Class.
"""

from ursina import Entity, Vec3, scene

from ..constants import WORLD_SIZE
from src.game.voxel import Voxel


class Ground(Entity):
    """
    Class to represent the ground.
    """

    def __init__(self) -> None:
        """
        Constructor used to initialize some values.
        """
        self._set_entity()
        self._set_ground_entities()

    def _set_entity(self) -> None:
        """
        Private Method to set up the ground entity.
        """
        ground_attributes = {"parent": scene}

        super().__init__(**ground_attributes)

    def _set_ground_entities(self) -> None:
        """
        Private Method to set up the ground-related entities.
        """
        self._set_voxels()

    def _set_voxels(self) -> None:
        """
        Private Method to set up the voxels.
        """
        for z in range(WORLD_SIZE):
            for x in range(WORLD_SIZE):
                self._create_voxel(x, z)

    def _create_voxel(self, x: int, z: int) -> None:
        """
        Private Method create a voxel.

        Parameters
        ----------
        x : int
            The voxel's X position

        z : int
            The voxel's z position
        """
        voxel_position = Vec3(x, 0, z)

        voxel_attributes = {"position": voxel_position}

        Voxel(**voxel_attributes)
