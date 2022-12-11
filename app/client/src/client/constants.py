"""
Module containing some server constants.
"""

from random import randint


CLIENT_HOST = "localhost"
CLIENT_PORT = randint(8_000, 9_000)
CLIENT_ADDRESS = (CLIENT_HOST, CLIENT_PORT)


SERVER_HOST = "localhost"
SERVER_PORT = 25565
SERVER_ADDRESS = (SERVER_HOST, SERVER_PORT)
