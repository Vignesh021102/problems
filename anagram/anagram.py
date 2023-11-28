def _get_char_frequencies(string):
    """
    Get the frequency of characters in a string.

    Args:
        string (str): The input string.

    Returns:
        dict: A dictionary containing the frequency of each character in the string.
    """
    char_freq = {}
    for char in string:
        char_freq[char] = char_freq.get(char, 0) + 1
    return char_freq

def are_char_frequencies_equal(string1: str, string2: str) -> bool:
    """
    Check if two strings have the same frequency of characters.

    Args:
        string1 (str): The first string.
        string2 (str): The second string.

    Returns:
        bool: True if the frequency of characters in string1 is equal to the frequency of characters in string2, False otherwise.
    """
    return _get_char_frequencies(string1) == _get_char_frequencies(string2)