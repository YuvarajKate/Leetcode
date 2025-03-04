class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)  # Create a set from the list
        longest_streak = 0   # Variable to store the longest streak found

        for num in num_set:
            # Check if it's the start of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                
                # Count the length of the consecutive sequence
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                
                # Update the longest streak if current streak is longer
                longest_streak = max(longest_streak, current_streak)

        return longest_streak