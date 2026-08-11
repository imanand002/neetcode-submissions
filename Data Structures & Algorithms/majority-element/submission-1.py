class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n: int = len(nums)
        #unique_list: list = list(set(nums))
        # i = 0
        # current = nums[i]
        # count = 0

        # for i in range(len(nums)):
        #     if current == nums[i]:
        #         count += 1
        #         i += 1
        
        # if count > (n//2):
        #     return current
        sort_arr: list = list(sorted(nums))

        ans = sort_arr[n//2]
        return ans
        
        