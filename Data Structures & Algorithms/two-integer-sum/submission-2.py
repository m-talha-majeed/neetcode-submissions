class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        empty_map={}
        i=0
        for num in nums:
            if num in empty_map:
                return [empty_map[num],i]
            else:
                empty_map[target-num]=i
            i=i+1