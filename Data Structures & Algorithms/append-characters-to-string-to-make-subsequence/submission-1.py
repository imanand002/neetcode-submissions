class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = j = 0
        for i in range(len(s)):
            if j >= len(t):
                break
            if (s[i] == t[j]):
                j += 1
        
        if len(t) == j:
            return 0

        return len(t) - j