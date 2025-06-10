import os
from save_utils import save_txt, save_docx


def test_save_txt():
    conversation = [("User", "Hello"), ("Bot", "Hi there!")]
    filename = "test_conversation.txt"
    save_txt(conversation, filename)
    assert os.path.exists(filename), "Plik TXT nie został zapisany"
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
        assert "User: Hello" in content
        assert "Bot: Hi there!" in content
    os.remove(filename)


def test_save_docx():
    from docx import Document
    conversation = [("User", "Cześć"), ("Bot", "Witaj!")]
    filename = "test_conversation.docx"
    save_docx(conversation, filename)
    assert os.path.exists(filename), "Plik DOCX nie został zapisany"
    doc = Document(filename)
    text = "\n".join([p.text for p in doc.paragraphs])
    assert "User: Cześć" in text
    assert "Bot: Witaj!" in text
    os.remove(filename)


if __name__ == "__main__":
    test_save_txt()
    test_save_docx()
    print("✅ Wszystkie testy zaliczone.")
