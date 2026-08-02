class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count: int = 0
        for i in range(len(details)):
            # sliced the age and convert it to int as > can't work b/w int and str
            if int(details[i][11:13]) > 60:
                count += 1
        
        return count