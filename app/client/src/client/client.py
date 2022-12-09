"""
Module containing the "Client" Class.
"""

from ursinanetworking import UrsinaNetworkingClient, EasyUrsinaNetworkingClient

from .constants import CLIENT_HOST, CLIENT_PORT


client = UrsinaNetworkingClient(CLIENT_HOST, CLIENT_PORT)


@client.event
def onConnectionEstablished():
    """"""
    print("I'm connected to the server!")


@client.event
def onConnectionError(error):
    print("I'm disconnected =(")
    print(f"ERROR TYPE: {type(error)}")
    print(f"ERROR: {error}")


class GameClient:
    """
    Class to represent the game client.
    """

    client: EasyUrsinaNetworkingClient

    def __init__(self) -> None:
        self.client = EasyUrsinaNetworkingClient(client)

    def start(self) -> None:
        """"""
        self.client.process_net_events()

    def send_to_server(self, message: str) -> None:
        """"""
        client.send_message("request_destroy_block", message)
