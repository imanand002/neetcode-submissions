class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = s.split()
        last_word_of_arr = list(arr[-1])
        return len(last_word_of_arr)