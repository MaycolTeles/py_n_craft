"""
Module containing the "Message" dataclass.
"""

from dataclasses import dataclass

from ..clients.client import Client


@dataclass
class Message:
    tag: str
    message: str
    client: Client
