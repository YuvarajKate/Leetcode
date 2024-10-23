class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start: int, current_combination: List[int], remaining_target: int):
            if remaining_target == 0:  # Found a valid combination
                result.append(current_combination[:])  # Add a copy of the current combination
                return
            if remaining_target < 0:  # Exceeded the target, no valid combination
                return
            
            for i in range(start, len(candidates)):
                current_combination.append(candidates[i])  # Choose the candidate
                backtrack(i, current_combination, remaining_target - candidates[i])  # Recur with reduced target
                current_combination.pop()  # Backtrack: remove the last added candidate

        result = []
        backtrack(0, [], target)  # Start backtracking with an empty combination and the full target
        return result