class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        arr=[[]]
        for i in nums:
            for j in list(arr):
                b=j+[i]
                arr.append(b)
        return arr