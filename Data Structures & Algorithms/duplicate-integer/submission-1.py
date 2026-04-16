class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # seen = []

        # for i in range(len(nums)):
        #     if nums[i] not in seen:
        #         seen.append(nums[i])

        seen = set(nums)
        if len(seen) < len(nums):
            return True
        else: 
            return False

if __name__ == '__main__':
    obj = Solution()
    result = obj.hasDuplicate([1,2,5,3])
    print(result)