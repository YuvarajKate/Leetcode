class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pmap = {}
        for i, n in enumerate(nums):
            x = target - n
            if x in pmap:
                return [pmap[x] , i]
            
            pmap[n] = i
            