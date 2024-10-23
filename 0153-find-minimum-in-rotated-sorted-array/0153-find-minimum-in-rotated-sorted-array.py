class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        # Perform binary search
        while left < right:
            mid = left + (right - left) // 2
            
            # If the middle element is greater than the rightmost element,
            # the minimum must be in the right half (this means the left half is sorted)
            if nums[mid] > nums[right]:
                left = mid + 1
            
            # Otherwise, the minimum must be in the left half
            else:
                right = mid
        
        # After the loop, left == right, which will be the index of the minimum element
        return nums[left]        