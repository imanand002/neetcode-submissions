class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # ans: List = []
        for num in range(len(nums)):
            nums.append(nums[num])
        
        ans = nums
        return ans