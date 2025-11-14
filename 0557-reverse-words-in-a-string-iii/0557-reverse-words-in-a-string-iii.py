class Solution:
    def reverseWords(self, s: str) -> str:
        l  = s.split(" ")
        reversed_s = [i[::-1] for i in l]
        return " ".join(reversed_s)