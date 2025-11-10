class Solution:
    def isPalindrome(self, s: str) -> bool:
        ls = ""
        for i in s:
            if i.isalnum():
                ls += i.lower()
        return ls == ls[::-1]
    