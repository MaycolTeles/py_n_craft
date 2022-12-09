"""
Module containing the "Sky" Class.
"""
from ursina import Entity, scene


class Sky(Entity):
    """
    Class to represent the sky.
    """

    def __init__(self) -> None:
        """
        Constructor used to initialize some values.
        """
        self._set_entity()

    def _set_entity(self) -> None:
        """
        Private Method to set up the ground entity.
        """
        sky_attributes = {
            "parent": scene,
            "model": "sphere",
            "texture": "assets/textures/sky/skybox.png",
            "scale": 200,
            "double_sided": True,
        }

        super().__init__(**sky_attributes)
