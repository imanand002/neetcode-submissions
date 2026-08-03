class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s = s.reverse()
        
    def reverseString(self, s: List[str]):
        i: int = 0
        j: int = len(s) - 1
        #  print(s[i], s[j])
        
        while(i < j):
            temp = s[i]
            s[i] = s[j]
            s[j] = temp

            i += 1
            j -= 1
