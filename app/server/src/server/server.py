"""
Module containing the "Server" Class.
"""

from ursina import Entity

from ursinanetworking import (
    UrsinaNetworkingServer,
    EasyUrsinaNetworkingServer,
    UrsinaNetworkingConnectedClient,
)

from .constants import SERVER_HOST, SERVER_PORT


server = UrsinaNetworkingServer(SERVER_HOST, SERVER_PORT)


@server.event
def onClientConnected(client: UrsinaNetworkingConnectedClient) -> None:
    """ """
    print(f"Client {client} connected!")


@server.event
def onClientDisconnected(client: UrsinaNetworkingConnectedClient) -> None:
    """"""
    print(f"Client {client} disconnected!")


# DECLARING A SERVER EVENT
@server.event
def request_destroy_block(client: UrsinaNetworkingConnectedClient, block_name: str):
    """
    Function to declare a server event.

    This event is triggered when a player (client) tries to destroy a block.
    """
    game_server.destroy_block(block_name)


# DECLARING A SERVER EVENT
@server.event
def request_create_block(client: UrsinaNetworkingConnectedClient, block: Entity):
    """
    Function to declare a server event.

    This event is triggered when a player (client) tries to destroy a block.
    """
    game_server.create_block(block)


class GameServer:
    """"""

    _server: EasyUrsinaNetworkingServer

    def __init__(self) -> None:
        """"""
        self._server = EasyUrsinaNetworkingServer(server)

    def start(self) -> None:
        """"""
        while True:
            self._server.process_net_events()

    def destroy_block(self, block: Entity):
        """
        Method to broadcast that the block should be destroyed.
        """
        self._server.remove_replicated_variable_by_name(block)

    def create_block(self, block: Entity) -> None:
        """"""
        self._server.create_replicated_variable(block)


game_server = GameServer()
