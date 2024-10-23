class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:  # If the input is empty, return an empty list
            return []
        
        # Mapping of digits to letters
        phone_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        result = []  # List to store the combinations

        def backtrack(index: int, current_combination: str):
            if index == len(digits):  # If the current combination is complete
                result.append(current_combination)  # Add it to the result
                return
            
            # Get the letters corresponding to the current digit
            letters = phone_map[digits[index]]
            for letter in letters:
                # Add the letter to the current combination and move to the next digit
                backtrack(index + 1, current_combination + letter)

        backtrack(0, '')  # Start backtracking with the first digit
        return result