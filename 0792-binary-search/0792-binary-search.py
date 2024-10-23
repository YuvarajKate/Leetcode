class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        # While the search space is valid
        while left <= right:
            # Calculate the middle index
            mid = left + (right - left) // 2
            
            # If the target is found at the mid index, return the index
            if nums[mid] == target:
                return mid
            
            # If the target is smaller than the mid element, narrow the search to the left half
            elif target < nums[mid]:
                right = mid - 1
            
            # If the target is larger, narrow the search to the right half
            else:
                left = mid + 1
        
        # If the target is not found, return -1
        return -1