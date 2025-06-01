# save_utils.py
from docx import Document


def save_txt(conversation, filename="conversation.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for speaker, text in conversation:
            f.write(f"{speaker}: {text}\n")


def save_docx(conversation, filename="conversation.docx"):
    doc = Document()
    for speaker, text in conversation:
        doc.add_paragraph(f"{speaker}: {text}")
    doc.save(filename)
