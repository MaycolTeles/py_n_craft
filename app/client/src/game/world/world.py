"""
Module containing the "World" Class.
"""

from ursina import Entity, scene

from .ground import Ground
from .sky import Sky


class World(Entity):
    """
    Class to represent the world entity.
    """

    def __init__(self) -> None:
        """
        Constructor used to initialize some values.
        """
        self._set_entity()
        self._set_world_entities()

    def _set_entity(self) -> None:
        """
        Private Method to set up the world entity.
        """
        world_attributes = {"parent": scene}

        super().__init__(**world_attributes)

    def _set_world_entities(self) -> None:
        """
        Private Method to set up all the world-related entities.
        """
        self._ground = Ground()
        self._sky = Sky()
