import string
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_check={}
        for letter in s:
            if letter in hash_check:
                hash_check[letter]= hash_check[letter]+1 
            else:  
                hash_check[letter]=1
        for letter in t:
            if letter not in hash_check:
                return False
            else: 
                hash_check[letter]=hash_check[letter]-1
        for i in range(26):
            if string.ascii_lowercase[i] in hash_check and hash_check[string.ascii_lowercase[i]]!=0:
                return False
        return True