class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)

        for i in range(n):
            count += self.expandAroundCenter(s, i, i)   # Odd length palindromes
            count += self.expandAroundCenter(s, i, i + 1)  # Even length palindromes

        return count

    def expandAroundCenter(self, s: str, left: int, right: int) -> int:
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count