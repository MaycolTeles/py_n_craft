"""
Module containing the "Voxel" Class.
"""

from typing import Any

from ursina import Entity, Vec3, destroy, scene

from .textures import VoxelTextures


class Voxel(Entity):
    """
    Class to represent the voxel.
    """

    def __init__(self, **voxel_parameters: dict[str, Any]) -> None:
        """
        Constructor used to initialize some values.

        Parameters
        ----------
        voxel_parameters : dict[str, Any]
            The parameters to create the voxel
        """
        self._set_entity(voxel_parameters)

    def handle_click(self) -> None:
        """
        Method to handle the voxel when it gets clicked.
        """
        destroy(self)

    def _set_entity(self, voxel_parameters: dict[str, Any]) -> None:
        """
        Private Method to set up the voxel entity.

        Parameters
        ----------
        voxel_parameters : dict[str, Any]
            The parameters to create the voxel
        """
        parent = voxel_parameters.get("parent", scene)
        position = voxel_parameters.get("position", Vec3(0, 0, 0))
        texture = voxel_parameters.get("texture", VoxelTextures.GRASS.value)
        scale = voxel_parameters.get("scale", 0.5)
        rotation = voxel_parameters.get("rotation", Vec3(0, 0, 0))

        voxel_attributes = {
            "parent": parent,
            "model": "assets/models/voxel/block.obj",
            "texture": texture,
            "collider": "box",
            "position": position,
            "origin_y": 0.5,
            "scale": scale,
            "rotation": rotation,
        }

        super().__init__(**voxel_attributes)
