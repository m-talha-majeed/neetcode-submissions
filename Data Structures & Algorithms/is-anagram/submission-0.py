class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr=[0]*26
        for i in range(len(s)):
            num=ord(s[i])%26
            arr[num]+=1
        for i in range(len(t)):
            num=ord(t[i])%26
            arr[num]-=1
        for i in range(len(arr)):
            if arr[i]!=0:
                return False
        return True
