class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        def rob_linear(houses: List[int]) -> int:
            first, second = 0, 0
            for amount in houses:
                first, second = second, max(second, first + amount)
            return second
        
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))