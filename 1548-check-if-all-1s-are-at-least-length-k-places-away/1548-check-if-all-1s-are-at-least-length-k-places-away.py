class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        previous = -inf
        check = True
        for i in range(len(nums)):
            if nums[i] == 1:
                if previous != -1 and i - previous - 1 < k:
                    check = False
                    break
                previous = i
        else:
            check = True
        return check

            