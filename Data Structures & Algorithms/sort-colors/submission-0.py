class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i: int = 0
        j: int = 1

        for i in range(len(nums)): 
            j = i + 1

            # Inside while loop, first pass happens till j < len(nums)
            # and when the while loop condition met, it simply increase j
            # by i + 1 -> second pass and so on
            while j < len(nums):
                if nums[i] > nums[j]:
                    temp = nums[j]
                    nums[j] = nums[i]
                    nums[i] = temp
                j += 1
 

            

            