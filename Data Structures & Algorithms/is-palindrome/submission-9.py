class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr: str = ''
        for char in s:
            if char.isalnum():
                newStr = newStr + char.lower()
            
        return newStr == newStr[::-1]

        # cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', s)
        # arr = list(cleaned_text)
        # new_list = [item.lower() for item in arr]
        # reverse_arr = new_list[::-1]
        
        # if new_list == reverse_arr:
        #     return True
        # else: 
        #     return False