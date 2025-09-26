class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D': 500, 'M':1000}

        num = 0

        current = 0
        previous = 0

        for i in reversed(s):
            current = roman[i]
            if current < previous:
                num = num - current
            else:
                num = num + current
                previous = current
        return num