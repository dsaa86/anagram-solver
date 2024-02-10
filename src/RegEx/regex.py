import regex

def sanitiseAnagramString(anagram: str, pattern: str = r"[^a-z]+", err_msg: str = "Anagram must only contain letters (a-z, A-Z)") -> str:
    if type(anagram) != str:
        raise TypeError("Anagram must be a string")
    
    anagram = anagram.lower()

    regex_search = re.findall(pattern, anagram)
    if regex_search:
        raise ValueError("Anagram must only contain letters (a-z, A-Z)")

    return anagram


def preparePatternForMatching(pattern:str) -> str:
    
    if type(pattern) != str:
        raise TypeError("Pattern must be a string")
    
    prepared_pattern = r"^"
    
    for char in pattern:
        prepared_pattern += r"[a-z]" if char in ["_", "-"] else char
        
    prepared_pattern += r"$"

    return prepared_pattern