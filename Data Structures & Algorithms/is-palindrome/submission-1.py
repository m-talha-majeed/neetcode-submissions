class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_text = "".join(filter(str.isalnum, s)).lower()
        start = 0
        end = len(clean_text) - 1 
        while end > start:
            if clean_text[start] == clean_text[end]:
                start = start + 1
                end = end - 1
            else: 
                return False  
        return True
