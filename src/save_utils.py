"""
save_utils.py

Provides utilities for saving chat conversation data to various formats (TXT, DOCX, JSON),
as well as class-based saving support using an abstract base saver.
"""

from docx import Document
import json
from typing import List, Tuple, Callable, Any


def log_save(func: Callable) -> Callable:
    """
    Decorator for logging save operations.

    :param func: The function to wrap.
    :return: Wrapped function with logging.
    """

    def wrapper(*args, **kwargs):
        print(f"\U0001F4DD Zapis: {func.__name__}({args}, {kwargs})")
        return func(*args, **kwargs)

    return wrapper


@log_save
def save_txt(conversation: List[Tuple[str, str]], filename: str = "conversation.txt") -> None:
    """
    Save the conversation as a plain text (.txt) file.

    :param conversation: A list of (speaker, message) tuples.
    :param filename: Output file name (default: 'conversation.txt').
    """
    with open(filename, "w", encoding="utf-8") as f:
        for speaker, text in conversation:
            f.write(f"{speaker}: {text}\n")


@log_save
def save_docx(conversation: List[Tuple[str, str]], filename: str = "conversation.docx") -> None:
    """
    Save the conversation as a Word document (.docx).

    :param conversation: A list of (speaker, message) tuples.
    :param filename: Output file name (default: 'conversation.docx').
    """
    doc = Document()
    for speaker, text in conversation:
        doc.add_paragraph(f"{speaker}: {text}")
    doc.save(filename)


@log_save
def save_json(conversation: List[Tuple[str, str]], filename: str = "conversation.json") -> None:
    """
    Save the conversation as a JSON file.

    :param conversation: A list of (speaker, message) tuples.
    :param filename: Output file name (default: 'conversation.json').
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(conversation, f, ensure_ascii=False, indent=2)


def apply_to_conversation(conversation: List[Tuple[str, str]], func: Callable[[Tuple[str, str]], Any]) -> List[Any]:
    """
    Apply a function to each entry in the conversation.

    :param conversation: A list of (speaker, message) tuples.
    :param func: A function to apply to each conversation entry.
    :return: A list of transformed entries.
    """
    return [func(entry) for entry in conversation]


class MessageSaver:
    """
    Abstract base class for saving a conversation.

    Subclasses should implement the save() method.
    """

    def __init__(self, conversation: List[Tuple[str, str]]):
        """Initialize with conversation data."""
        self.conversation = conversation

    def save(self) -> None:
        """
        Save method placeholder. Should be implemented by subclasses.
        """
        raise NotImplementedError("Implement in a subclass")


class TxtSaver(MessageSaver):
    """
    Concrete class for saving a conversation to a TXT file.
    """

    def save(self, filename: str = "conversation_by_class.txt") -> None:
        """
        Save the conversation to a TXT file.

        :param filename: Output file name (default: 'conversation_by_class.txt').
        """
        with open(filename, "w", encoding="utf-8") as f:
            for speaker, text in self.conversation:
                f.write(f"{speaker}: {text}\n")
