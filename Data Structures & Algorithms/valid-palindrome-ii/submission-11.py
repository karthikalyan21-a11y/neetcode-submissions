class Solution:
    def validPalindrome(self, s: str) -> bool:
        low,high=(0,len(s)-1)
        def check(low,high):
            while low<=high:

                if s[low]!=s[high]:
                    return False
                low+=1
                high-=1
            return True
           
        while low<high:
            if s[low]!=s[high]:
                return check(low+1,high) or check(low,high-1)
       
            low+=1
            high-=1
        return True

                

        