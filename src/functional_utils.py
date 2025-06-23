"""
conversation_utils.py

This module provides utility functions for processing and analyzing chat conversations.
It includes transformations, filters, aggregations, and search operations based on
functional programming paradigms such as map, filter, and reduce.
"""

from functools import reduce
from typing import List, Tuple, Set


def uppercase_conversation(conversation: List[Tuple[str, str]]) -> List[Tuple[str, str]]:
    """
    Convert all message texts in the conversation to uppercase.

    :param conversation: A list of (speaker, message) tuples.
    :type conversation: List[Tuple[str, str]]
    :return: New list with all message texts converted to uppercase.
    :rtype: List[Tuple[str, str]]
    """
    return list(map(lambda entry: (entry[0], entry[1].upper()), conversation))


def only_user_messages(conversation: List[Tuple[str, str]]) -> List[Tuple[str, str]]:
    """
    Filter the conversation to return only messages sent by the user.

    :param conversation: A list of (speaker, message) tuples.
    :type conversation: List[Tuple[str, str]]
    :return: List of user messages only.
    :rtype: List[Tuple[str, str]]
    """
    return list(filter(lambda entry: entry[0] == "Użytkownik", conversation))


def total_chars(conversation: List[Tuple[str, str]]) -> int:
    """
    Calculate the total number of characters in all messages in the conversation.

    :param conversation: A list of (speaker, message) tuples.
    :type conversation: List[Tuple[str, str]]
    :return: The total character count of all messages.
    :rtype: int
    """
    return reduce(lambda acc, entry: acc + len(entry[1]), conversation, 0)


def get_unique_speakers(conversation: List[Tuple[str, str]]) -> Set[str]:
    """
    Extract a set of unique speaker identifiers from the conversation.

    :param conversation: A list of (speaker, message) tuples.
    :type conversation: List[Tuple[str, str]]
    :return: Set of unique speaker names.
    :rtype: Set[str]
    """
    return set(entry[0] for entry in conversation)


def search_messages(conversation: List[Tuple[str, str]], keyword: str) -> List[Tuple[str, str]]:
    """
    Search for messages containing a specific keyword (case-insensitive).

    :param conversation: A list of (speaker, message) tuples.
    :type conversation: List[Tuple[str, str]]
    :param keyword: Keyword to search for in message texts.
    :type keyword: str
    :return: List of messages containing the keyword.
    :rtype: List[Tuple[str, str]]
    """
    return list(filter(lambda entry: keyword.lower() in entry[1].lower(), conversation))
