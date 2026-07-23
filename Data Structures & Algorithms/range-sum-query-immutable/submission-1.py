class NumArray:

    # def __init__(self, nums: List[int]):
    #     self.nums = nums

    # def sumRange(self, left: int, right: int) -> int:
    #     count = 0
    #     for i in range(left, (right +1)):
    #         count = count + self.nums[i] 
    #         left += 1
        
    #     return count

    # prefix sum approach
    def __init__(self, nums: List[int]):
        self.prefix = []
        count = 0

        for num in nums:
            count = count + num 
            self.prefix.append(count)

    def sumRange(self, left, right):
        rightSum = self.prefix[right]
        leftSum = self.prefix[left - 1] if left > 0 else 0
        return rightSum - leftSum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)