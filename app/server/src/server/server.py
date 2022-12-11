"""
Module containing the "GameServer" Class.
"""

from typing import Any
import queue
import socket
import threading

from .constants import SERVER_ADDRESS, AVAILABLE_COMMANDS

# from .client import Client


class GameServer:
    """"""

    _socket: socket.socket
    _clients: list[str]
    _queue_messages: queue.Queue[tuple[str, Any]]

    def __init__(self) -> None:
        """
        Constructor to set up some variables.
        """
        self._set_up_socket_connection()
        self._clients = []
        self._queue_messages = queue.Queue()

    def start(self) -> None:
        """"""
        self._create_world()

        receive_thread = threading.Thread(target=self._receive_messages_from_clients)
        broadcast_thread = threading.Thread(
            target=self._broadcast_all_messages_to_all_clients
        )

        receive_thread.start()
        broadcast_thread.start()

    def _set_up_socket_connection(self) -> None:
        """
        Private Method to set up the socket connection.
        """
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._socket.bind(SERVER_ADDRESS)

    def _receive_messages_from_clients(self) -> None:
        """
        Private Method to receive messages from the clients.
        """
        while True:
            encoded_message, address = self._socket.recvfrom(1024)
            message = encoded_message.decode()

            print(f"MESSAGE RECEIVED: {message} - FROM CLIENT: {address}")
            self._process_client_message(message, address)

    def _process_client_message(self, message: str, address: str) -> None:
        """
        Private Method to process the message received from the client.
        """
        message_tag, message = message.split(":")
        # print("MESSAGE TAG: ", message_tag)
        # print("MESSAGE: ", message)

        # if message.startswith("[LOGIN]")
        # if address not in self._clients:
        #     self._add_client_to_connected_clients()
        #     self._clients.append(address)

        self._queue_messages.put((message, address))

    def _broadcast_all_messages_to_all_clients(self) -> None:
        """
        Private Method to broadcast all messages
        to all connected clients.
        """
        while True:
            while not self._queue_messages.empty():
                message, address = self._queue_messages.get()
                self._broadcast_message_to_all_clients(message, address)

    def _broadcast_message_to_all_clients(self, message: str, address: str) -> None:
        """"""
        message_is_valid = self._check_if_message_is_valid(message)

        if not message_is_valid:
            print("INVALID COMMAND: ", message)

        for client in self._clients:
            self._broadcast_message_to_client(message, client)

    def _broadcast_message_to_client(self, message: str, client: str) -> None:
        """
        Private Method to broadcast the message received as argument
        to the connected client received as argument.
        """
        encoded_message = message.encode()

        # print(f"SENDING MESSAGE: {message} - TO CLIENT {client}")
        self._socket.sendto(encoded_message, client)

    def _check_if_message_is_valid(self, message: str) -> bool:
        """
        Private Method to check whether the message received as argument
        is valid or not.
        """
        return message.startswith(AVAILABLE_COMMANDS)

    def _create_world(self) -> None:
        """
        Private Method to create the world.
        """
        # print('CREATING WORLD!')

    # @self._server.event
    # def onClientConnected(self, client: UrsinaNetworkingConnectedClient) -> None:
    #     """"""
    #     print(f"Client {client} connected!")
    #     self._clients.append(client)

    # @self._server.event
    # def onClientDisconnected(self, client: UrsinaNetworkingConnectedClient) -> None:
    #     """"""
    #     print(f"Client {client} disconnected!")
    #     self._clients.remove(client)


# @server_events.event
# def send_to_all_clients(message: str) -> None:
#     """
#     Method to send a message to all connected clients.
#     """
#     server_events.broadcast(message)
