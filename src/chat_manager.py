"""
chat_manager.py

This module provides the ChatManager class to manage chat conversation storage
and manipulation. It supports adding, retrieving, and clearing messages,
with a design that facilitates documentation generation and diagramming.
"""
from typing import List, Tuple


class ChatManager:
    """
    Manage storage and operations on a chat conversation.

    Attributes:
        convo (List[Tuple[str, str]]): List of (speaker, message) tuples representing the conversation.
    """

    def __init__(self) -> None:
        """
        Initialize an empty conversation history.
        """
        self.convo: List[Tuple[str, str]] = []

    def add(self, speaker: str, message: str) -> None:
        """
        Add a new message to the conversation history.

        :param speaker: Identifier of the message sender.
        :type speaker: str
        :param message: The content of the message.
        :type message: str
        :return: None
        """
        self.convo.append((speaker, message))

    def get(self) -> List[Tuple[str, str]]:
        """
        Retrieve the full conversation history.

        :return: List of (speaker, message) tuples.
        :rtype: List[Tuple[str, str]]
        """
        return self.convo

    def clear(self) -> None:
        """
        Remove all messages from the conversation history.

        :return: None
        """
        self.convo.clear()
