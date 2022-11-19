"""
Napisz funkcje sprawdzającą czy dane słowo jest palindromem
Hint: Palindrom to słowo brzmiące od przodu jak i od tyłu tak samo
"""

def is_palindrom(text: str) -> bool:
    """
    Funkcja sprawdzająca czy dany tekst jest palindromem.
    Args:
        text: tekst

    Returns:
        boolean: czy teskt jest palindromem
    """
    pass

assert is_palindrom("ala") == True
assert is_palindrom("Oka") == False
assert is_palindrom("OkO") == True
assert is_palindrom("A to idiOta") == True
assert is_palindrom("A to idiota!") == True