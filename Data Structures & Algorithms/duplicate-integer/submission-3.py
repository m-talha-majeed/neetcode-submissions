class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         arr={}
         for i in range(len(nums)):
            if nums[i] in arr.keys():
                return True
            else:
                arr[nums[i]]=i
         return False