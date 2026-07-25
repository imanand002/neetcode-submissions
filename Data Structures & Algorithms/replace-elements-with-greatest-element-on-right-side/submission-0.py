class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # initial max = -1
        # reverse iteration
        # new max = max(oldmax, arr[i])
        rightMax = -1
        # [17,18,5,4,6,1]
        for i in range(len(arr)-1, -1, -1 ): #range(start, stop, step)
            # currently the pointer i is at 1 in the array
            new_max = max(arr[i], rightMax)
            arr[i] = rightMax
            rightMax = new_max
        return arr

            