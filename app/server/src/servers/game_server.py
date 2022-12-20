"""
Module containing the "GameServer" Class.
"""

from typing import Any
import queue
import socket
import sys
import time
import threading

from server.src.constants import SERVER_ADDRESS, SERVER_TICK_FREQUENCY
from server.src.user_interfaces import CLI


class GameServer:
    """"""

    _is_running: bool
    _running_lock: threading.Lock
    _tick_count: int
    _socket: socket.socket
    _clients: list[str]
    _queue_messages: queue.Queue[tuple[str, Any]]

    def __init__(self) -> None:
        """
        Constructor to set up some variables.
        """
        self._set_up_socket_connection()
        self._set_up_attributes()

    @property
    def is_running(self) -> bool:
        """"""
        is_running = False

        with self._running_lock:
            is_running = self._is_running

        return is_running

    @is_running.setter
    def is_running(self, running_status: bool) -> None:
        """"""
        with self._running_lock:
            self._is_running = running_status

    def start(self) -> None:
        """
        Method to start the server.
        """
        self.is_running = True

        print()
        print(f"> SERVER RUNNING ON {SERVER_ADDRESS}", end="\n\n")

        # self._create_world()

        self._start_threads()
        self._run_cli()

    def shut_down(self) -> None:
        """
        Method to shut down the server.
        """
        self.is_running = False

        self._socket.close()

        self._ticks_thread.join()
        self._accept_connection_thread.join()

        # self._receive_thread.join()
        # self._broadcast_thread.join()

        print("> SERVER OFF")
        sys.exit()

    def _set_up_attributes(self) -> None:
        """"""
        self._tick_count = 0
        self._running_lock = threading.Lock()
        self._last_tick_time = time.time()
        self.is_running = False
        self._clients = []
        # self._queue_messages = queue.Queue()

    def _start_threads(self) -> None:
        """"""
        self._ticks_thread = threading.Thread(target=self._start_running_ticks)
        self._accept_connection_thread = threading.Thread(
            target=self._accept_new_connection
        )

        # self._receive_thread = threading.Thread(
        # target=self._start_receiving_messages_from_clients
        # )
        # self._broadcast_thread = threading.Thread(
        # target=self._start_broadcasting_messages_to_clients
        # )

        self._ticks_thread.start()
        self._accept_connection_thread.start()

        # self._receive_thread.start()
        # self._broadcast_thread.start()

    def _run_cli(self) -> None:
        """"""
        cli = CLI(self)

        while self.is_running:
            cli.run()

        self.shut_down()

    def _start_running_ticks(self) -> None:
        """"""
        while self.is_running:
            wait_time = 1 / SERVER_TICK_FREQUENCY
            elapsed_time = time.time() - self._last_tick_time

            if elapsed_time < wait_time:
                remaining_time = wait_time - elapsed_time
                time.sleep(remaining_time)

            self._last_tick_time = time.time()
            self._tick()

    def _tick(self) -> None:
        """"""
        self._tick_count += 1

    def _set_up_socket_connection(self) -> None:
        """
        Private Method to set up the socket connection.
        """
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.bind(SERVER_ADDRESS)

        # Enable server to accept connections
        self._socket.listen()

    def _start_receiving_messages_from_clients(self) -> None:
        """"""
        while self.is_running:
            pass
            # TODO: FIX. TÁ DANDO PAU NA THREAD
            # client_message = self._get_client_message()
            # self._process_client_message(client_message)

    def _accept_new_connection(self) -> None:
        """
        Private Method to run while the server is active and block to listen to
        new connections. Once it's found, starts a new thread to it.
        """
        while self.is_running:
            try:
                connection, address = self._socket.accept()

                self._add_new_client(connection, address)
            except socket.error as error:
                print("AN ERROR OCCURED WHILE TRYING TO ACCEPT A NEW CLIENT")
                print(f"ERROR: {error}")

    def _add_new_client(self, connection: str, address: str) -> None:
        """"""
        print("CLIENT ADDED!")
        print("CONNECTION: ", connection)
        print("ADDRESS: ", address)

        self._clients.append((connection, address))

    def _get_client_message(self) -> tuple[str, str]:
        """"""
        # ACHO que enquanto eu nao enviar uma msg, esse cara aqui fica travado
        encoded_message, address = self._socket.recvfrom(1024)
        message = encoded_message.decode()

        # message = Message()

        return message, address

    def _process_client_message(self, client_message: Any) -> None:
        """
        Private Method to process the message received from the client.
        """
        # message_tag, message = self._split_into_tag_and_message(message)

        # print("MESSAGE TAG: ", message_tag)
        # print("MESSAGE: ", message)

        # if message.startswith("[LOGIN]")
        # if address not in self._clients:
        #     self._add_client_to_connected_clients()
        #     self._clients.append(address)

        self._queue_messages.put(client_message)

    def _start_broadcasting_messages_to_clients(self) -> None:
        """"""
        while self.is_running:
            while not self._queue_messages.empty():
                message, address = self._queue_messages.get()
                self._broadcast_message_to_all_clients(message, address)

    def _broadcast_message_to_all_clients(self, message: str, address: str) -> None:
        """"""
        for client in self._clients:
            self._broadcast_message_to_client(message, client)

    def _broadcast_message_to_client(self, message: str, client: str) -> None:
        """
        Private Method to broadcast the message received as argument
        to the connected client received as argument.
        """
        encoded_message = message.encode()
        self._socket.sendto(encoded_message, client)

    # def _check_if_tag_is_valid(self, tag: str) -> bool:
    #     """
    #     Private Method to check whether the tag received as argument
    #     is a valid or not (i.e. the server accepts this command).
    #     """
    #     return tag in MessageTag.values()

    def _split_into_tag_and_message(self, string: str) -> tuple[str, str]:
        """
        Private Method to split the string received as argument into a
        message tag and the message.
        """
        tag, message = string.split(":")
        return tag, message

    # def _create_world(self) -> None:
    #     """
    #     Private Method to create the world.
    #     """
    #     # TODO: CREATE THE WORLD
    #     print('CREATING WORLD!')
