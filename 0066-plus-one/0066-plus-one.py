class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = "".join(map(str, digits))
        added = int(num)+1
        l = list(map(int, str(added)))
        return l