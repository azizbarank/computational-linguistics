"""
Utility functions shared across all problems.
"""


def load_corpus(file_path):
    """
    Load a text corpus from a file.

    Args:
        file_path: Path to the corpus file

    Returns:
        Text content as a string
    """
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()
