class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, 0, 0]

        for num in nums:
            for sum_val in list(dp):
                new_sum = sum_val + num
                remainder = new_sum % 3
                dp[remainder] = max(dp[remainder], new_sum)
        
        return dp[0]