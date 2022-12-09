"""
Module containing the "VoxelTextures" Enum.
"""

from enum import Enum

from ursina import Texture, load_texture


class VoxelTextures(Enum):
    """
    Enum containing all available voxel textures.
    """

    GRASS: Texture = load_texture("assets/textures/voxel/grass_block.png")
    STONE: Texture = load_texture("assets/textures/voxel/stone_block.png")
    DIRT: Texture = load_texture("assets/textures/voxel/dirt_block.png")
    BRICK: Texture = load_texture("assets/textures/voxel/brick_block.png")
