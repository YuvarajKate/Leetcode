class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        count = 0
        i = len(bits) - 2       # start just before the guaranteed last 0

        # count consecutive 1s backwards
        while i >= 0 and bits[i] == 1:
            count += 1
            i -= 1

        # if count of 1s is even → last char is 1-bit
        return (count % 2 == 0)
