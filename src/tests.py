"""
test_save_utils.py

Unit and performance tests for the save_utils module. Includes:
- Functional tests for TXT and DOCX saving
- Error handling validation
- Performance benchmarking
- Memory profiling

Run this script directly to execute all tests.
"""

import os
import timeit
from save_utils import save_txt, save_docx
from docx import Document
from memory_profiler import profile


@profile
def test_memory():
    """Memory profiling test for large TXT save."""
    conversation = [("Bot", "Hello")] * 1000
    save_txt(conversation, "mem_test.txt")
    os.remove("mem_test.txt")


def test_save_txt():
    """Test if conversation is correctly saved in TXT format."""
    conversation = [("User", "Hello"), ("Bot", "Hi there!")]
    filename = "test_conversation.txt"
    save_txt(conversation, filename)
    assert os.path.exists(filename), "TXT file was not saved"
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
        assert "User: Hello" in content
        assert "Bot: Hi there!" in content
    os.remove(filename)


def test_save_docx():
    """Test if conversation is correctly saved in DOCX format."""
    conversation = [("User", "Cześć"), ("Bot", "Witaj!")]
    filename = "test_conversation.docx"
    save_docx(conversation, filename)
    assert os.path.exists(filename), "DOCX file was not saved"
    doc = Document(filename)
    text = "\n".join([p.text for p in doc.paragraphs])
    assert "User: Cześć" in text
    assert "Bot: Witaj!" in text
    os.remove(filename)


def test_invalid_input():
    """Ensure function raises an error with invalid input format."""
    try:
        save_txt("not_a_list_of_tuples")
    except Exception as e:
        print("✅ Correctly caught error:", e)
    else:
        assert False, "Function did not raise an error for invalid input"


def test_performance():
    """Benchmark time required to save a large conversation."""
    conversation = [("Bot", "Test message")] * 1000
    duration = timeit.timeit(lambda: save_txt(conversation, "big_test.txt"), number=1)
    print(f"⏱️ Save time for 1000 messages: {duration:.4f}s")
    os.remove("big_test.txt")


if __name__ == "__main__":
    test_save_txt()
    test_save_docx()
    test_invalid_input()
    test_performance()
    print("✅ All tests passed.")
