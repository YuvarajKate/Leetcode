class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(current_permutation: List[int]):
            if len(current_permutation) == len(nums):  # All numbers are used
                result.append(current_permutation[:])  # Add a copy of the current permutation
                return
            
            for num in nums:
                if num in current_permutation:  # Skip used numbers
                    continue
                current_permutation.append(num)  # Add the number to the current permutation
                backtrack(current_permutation)    # Recur with the updated permutation
                current_permutation.pop()          # Remove the number to backtrack

        result = []
        backtrack([])  # Start backtracking with an empty permutation
        return result