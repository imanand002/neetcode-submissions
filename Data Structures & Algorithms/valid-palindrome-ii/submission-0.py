class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while(l < r):
            if s[l] != s[r]:
                skip_left = s[l + 1: r + 1]
                skip_right = s[l:r]
                return (skip_left == skip_left[::-1] or skip_right == skip_right[::-1])
            
            l, r = l + 1, r - 1
        
        return True

    #     if s == s[::-1]:
    #         return True

    #     for i in range(len(s)):
    #         new_str: str = s[:i] + s[i + 1:]
    #         if new_str == new_str[::-1]:
    #             return True
        
    #     return False
"""
Brute Force Approach:

1. Compare the original string with its reversed version, if true, return True
2. Next,loop the input string, and create a new string and delete the ith character from the input string by first slicing it upto i (which exludes i) then concatenate it with another slice ([i+1: ]). -> ith char sliced!
3. If the new string is equal to it reversed version, return true

Two Pointers approach: This approach is specifically for the mismatched characters and when mismatch happens it handles two cases, check the new string either after skipping the left or right character. And then compares the two left and right skipped char string with their own reversed version

1. l = 0 & r = len(s) -1.
2. if s[l] != s[r]
    skip_left
    skip_right

    return skip_left == reverse or skip_right == reverse
"""
        
