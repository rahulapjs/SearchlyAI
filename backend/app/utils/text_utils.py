import re


def clean_text(text: str) -> str:
    """
    Normalize text by removing excessive whitespace.
    """
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def is_valid_text(text: str, min_length: int = 50) -> bool:
    """
    Prevent embedding extremely small or empty text.
    """
    return bool(text and len(text.strip()) >= min_length)
