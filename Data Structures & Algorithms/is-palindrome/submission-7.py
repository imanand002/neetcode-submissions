class Solution:
    def isPalindrome(self, s: str) -> bool:
        input_str: str = s
        
        single_str: str = input_str.replace(" ","")
        
        new_lst = []

        for i in range(0, len(single_str)):
            if 'A' <= single_str[i] <= 'Z' or 'a' <= single_str[i] <= 'z' or '0' <= single_str[i] <= '9':
              new_lst.append(single_str[i])
        
        char = "".join(new_lst)
        
        small_case = char.lower()
        reversed_char = small_case[::-1]
        

        if small_case == reversed_char:
          return True
        else:
          return False

obj: object = Solution()
result = obj.isPalindrome('0P')
print(result)