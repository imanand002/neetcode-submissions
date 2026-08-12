class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_arr = list(set(nums))

        if len(unique_arr) != len(nums):
            return True
        else:
            return False