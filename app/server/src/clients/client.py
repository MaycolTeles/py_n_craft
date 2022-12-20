"""
Module containing the "Client" dataclass.
"""

from dataclasses import dataclass


@dataclass
class Client:
    name: str
    address: int
