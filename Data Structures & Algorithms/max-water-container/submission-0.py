class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum=0 
        start = 0 
        end= len(heights)-1 
        while start<end:
            result = min(heights[start],heights[end])
            local_maximum = (end - start) * result
            if heights[start] < heights[end]:
                start= start+1
            else:
                end=end-1 
            if local_maximum> maximum:
                maximum=local_maximum
        return maximum