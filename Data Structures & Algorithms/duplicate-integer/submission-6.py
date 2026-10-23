class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        empty_map={}
        for num in nums:
            if num in empty_map:
                return True
            else:
                empty_map[num]=1
        return False

        