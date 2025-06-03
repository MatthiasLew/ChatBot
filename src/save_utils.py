# save_utils.py

from docx import Document


def save_txt(conversation, filename="conversation.txt"):
    """
    Saves the conversation history to a plain text (.txt) file.

    Parameters:
    - conversation (list of tuples): A list of (speaker, text) pairs representing the dialogue.
    - filename (str): Optional; the name of the file to save. Defaults to "conversation.txt".

    Each message is written on a new line in the format:
    Speaker: Message
    """
    with open(filename, "w", encoding="utf-8") as f:
        for speaker, text in conversation:
            f.write(f"{speaker}: {text}\n")


def save_docx(conversation, filename="conversation.docx"):
    """
    Saves the conversation history to a Microsoft Word (.docx) file.

    Parameters:
    - conversation (list of tuples): A list of (speaker, text) pairs representing the dialogue.
    - filename (str): Optional; the name of the file to save. Defaults to "conversation.docx".

    Each message is added as a separate paragraph for readability.
    """
    doc = Document()
    for speaker, text in conversation:
        doc.add_paragraph(f"{speaker}: {text}")
    doc.save(filename)
