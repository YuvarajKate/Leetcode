class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)
        if len(y) < 2:
            return True
        else:
            l=0
            r=len(y)-1
            while l < r:
                if y[l]!=y[r]:
                    return False
                l += 1
                r -= 1        
            return True

        