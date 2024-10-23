class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start: int, current_subset: List[int]):
            result.append(current_subset[:])  # Add the current subset to the results
            
            for i in range(start, len(nums)):
                current_subset.append(nums[i])  # Include the current number
                backtrack(i + 1, current_subset)  # Recur for the next numbers
                current_subset.pop()  # Backtrack: remove the last added number

        result = []
        backtrack(0, [])  # Start backtracking with an empty subset
        return result