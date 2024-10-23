class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize the two pointers
        left, right = 0, len(nums) - 1
        
        # Perform binary search with additional logic to account for rotation
        while left <= right:
            mid = left + (right - left) // 2
            
            # If the target is found at the mid index, return the index
            if nums[mid] == target:
                return mid
            
            # Check which part is sorted
            # If the left part is sorted
            if nums[left] <= nums[mid]:
                # Check if the target is within the sorted part
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # Narrow search to the left
                else:
                    left = mid + 1   # Narrow search to the right
            
            # If the right part is sorted
            else:
                # Check if the target is within the sorted part
                if nums[mid] < target <= nums[right]:
                    left = mid + 1   # Narrow search to the right
                else:
                    right = mid - 1  # Narrow search to the left
        
        # If the target is not found, return -1
        return -1