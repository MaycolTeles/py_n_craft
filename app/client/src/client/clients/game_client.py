"""
Module containing the "Client" Class.
"""

import socket

from client.src.client.constants import SERVER_ADDRESS

# from shared.message_tag import MessageTag


class GameClient:
    """
    Class to represent the game client.
    """

    _socket: socket.socket

    def __init__(self) -> None:
        """
        Constructor to set up some variables.
        """
        self._set_up_socket_connection()

    def start(self) -> None:
        """"""
        self._connect_to_server()
        self._create_threads()

        self._socket.sendall(b"Hello, World!")
        # msg = self._socket.recv(1024)
        self._socket.close()

    def _set_up_socket_connection(self) -> None:
        """
        Private Method to set up the socket connection.
        """
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def _connect_to_server(self) -> None:
        """
        Private Method to connect to the server.
        """
        self._socket.connect(SERVER_ADDRESS)
        # server_message = self._build_message_to_server(MessageTag.SIGN_IN, message)

        # self._send_message_to_server(server_message)

    def _create_threads(self) -> None:
        """"""
        # receive_thread = threading.Thread(target=self._receive_messages_from_server)
        # broadcast_thread = threading.Thread(target=self._broadcast_message_to_server)

        # receive_thread.start()
        # broadcast_thread.start()

    # def _receive_messages_from_server(self) -> None:
    #     """ """
    #     while True:
    #         message, address = self._socket.recvfrom(1024)
    #         print(message, address)

    # def _broadcast_message_to_server(self) -> None:
    #     """"""
    #     while True:
    #         message = input("> ")

    #         server_message = self._build_message_to_server(MessageTag.TEXT, message)
    #         self._send_message_to_server(server_message)

    # def _build_message_to_server(self, message_tag: MessageTag, message: str) -> str:
    #     """"""
    #     return message_tag.value + ": " + message

    # def _send_message_to_server(self, message: str) -> None:
    #     """"""
    #     encoded_message = message.encode()
    #     self._socket.sendto(encoded_message, SERVER_ADDRESS)
