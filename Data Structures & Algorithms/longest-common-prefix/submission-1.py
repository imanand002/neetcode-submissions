class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # strs = ["bag", "bad", "bank", "band"]
        prefix: str = strs[0] # "bag"
        for i in range(1, len(strs)):
            j = 0
            while j < min(len(prefix), len(strs[i])): # min(3,3)
                if prefix[j] != strs[i][j]:
                    break
                j += 1
                #print(prefix)
            prefix = prefix[:j]
        return prefix