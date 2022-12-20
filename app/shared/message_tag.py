"""
Module containing the "MessageTag" Enum.
"""

from enum import Enum


class MessageTag(Enum):
    """"""

    SIGN_IN = "[SIGN_IN]"
    TEXT = "[TEXT]"
    MOVE = "[MOVE]"
    ATTACK = "[ATTACK]"
    INSERT = "[INSERT]"
    DELETE = "[DELETE]"

    @staticmethod
    def values() -> list[str]:
        """
        Method to return a list containing all available values for the enum.
        """
        return [item.value for item in MessageTag]
