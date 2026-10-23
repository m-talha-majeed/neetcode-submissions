class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap={}
        arr=[]
        index=0
        for string in strs:
            count = [0] * 26
            for letters in string:
                count[ord(letters) - ord('a')] += 1
            count_key = tuple(count)
                
            if count_key not in hashmap:
                hashmap[count_key] = index
                arr.append([string])  
                index = index + 1
            else:
                arr[hashmap[count_key]].append(string)
        return arr
                

        