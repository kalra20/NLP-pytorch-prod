import re
from typing import List

class REGEX:
    #regular expression matching
    def __init__(self) -> None:
        pass

    def text_match(self, text: str, pattern: str) -> str:
        """
        text = "The quick brown fox jumps over the lazy dog"
        pattern = "fox"
        return matching string
        
        """
        match = re.search(pattern, text)
        if match:
            return match.group()

    def split_str(self, text: str, delimiter: str) -> List[str]:
        """

        Example:
            text = "apple,banana, cherry, date"
            result = re.split(r',\s*', text) -> may throw a warning
            return list without delimiter
        """
        import re
        result = re.split(delimiter, text)
        return result

    def replace_match(self, text: str, pattern: str, replacement: str) -> str:
        """
        text = "The quick brown fox jumps over the lazy dog."
        pattern = "fox"
        replacement = "cat"
        
            
        return updated string
        
        """
        new_text = re.sub(pattern, replacement, text)
        print("Replaced text:", new_text)