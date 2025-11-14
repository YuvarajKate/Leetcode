class Solution:
    def reverseWords(self, s: str) -> str:
        l  = s.split(" ")
        reversed_s = ""
        for i in l:
            reversed_s += i[::-1]+" "
        return reversed_s.strip()