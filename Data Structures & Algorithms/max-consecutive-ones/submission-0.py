class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:   
        count = result = 0
        for nums in nums:
            count = count + 1 if nums else 0
            result = max(result, count)
        return result
