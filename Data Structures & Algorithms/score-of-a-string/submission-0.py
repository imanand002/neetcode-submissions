class Solution:
    def scoreOfString(self, s: str) -> int:
        score: int = 0
        i = 0
        j = 1

        while(i<len(s) and j < len(s)):
            score += abs(ord(s[i]) - ord(s[j]))
            print(score)

            i += 1
            j += 1

        return score
