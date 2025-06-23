"""
visualization.py

This module provides tools for visualizing aspects of a chat conversation.
Currently, it includes a function to plot the character length of each message over time.
"""

import matplotlib.pyplot as plt


def plot_lengths(conversation: list[tuple[str, str]]) -> None:
    """
    Generate and display a line plot showing the length of each message in a conversation.

    :param conversation: A list of (speaker, message) tuples, representing the conversation history.
                         Each tuple should contain the speaker label and the message content.
    :type conversation: list[tuple[str, str]]

    :return: None    :rtype:

    :effect: Saves a plot image ('message_lengths.png') and displays it using matplotlib.
             Useful for analyzing message size trends during interactions.
    """
    lengths = [len(message) for _, message in conversation]
    plt.plot(lengths, marker="o")
    plt.title("Message Length Over Time")
    plt.xlabel("Message Index")
    plt.ylabel("Character Count")
    plt.tight_layout()
    plt.savefig("message_lengths.png")
    plt.show()
