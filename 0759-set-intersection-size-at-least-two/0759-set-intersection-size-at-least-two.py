class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        
        # Sort intervals by end ASC, and start DESC
        intervals.sort(key=lambda x: (x[1], -x[0]))
        
        # last1 < last2 are the two largest numbers we selected so far
        last1 = -1_000_000_000
        last2 = -1_000_000_000
        
        count = 0
        
        for a, b in intervals:
            # Count how many of last1, last2 are inside the interval
            in_interval = 0
            if a <= last1 <= b:
                in_interval += 1
            if a <= last2 <= b:
                in_interval += 1
            
            # Case 1: Already have 2 points inside → do nothing
            if in_interval == 2:
                continue
            
            # Case 2: Only 1 point inside → add 1 point (b)
            elif in_interval == 1:
                count += 1
                # update last1/last2 appropriately
                last1 = last2
                last2 = b
            
            # Case 3: 0 points inside → add 2 points (b-1, b)
            else:
                count += 2
                last1 = b - 1
                last2 = b
        
        return count
