class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure that nums1 is the smaller array for binary search efficiency
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        half_len = (m + n + 1) // 2
        # Binary search over the smaller array
        left, right = 0, m
        while left <= right:
            # Partition nums1 and nums2
            partition1 = (left + right) // 2
            partition2 = half_len - partition1  
            # Handle edge cases where partition falls out of bounds
            max_left1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            min_right1 = float('inf') if partition1 == m else nums1[partition1]
            
            max_left2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            min_right2 = float('inf') if partition2 == n else nums2[partition2]
            # Check if we have found the correct partition
            if max_left1 <= min_right2 and max_left2 <= min_right1:
                # If the total number of elements is odd
                if (m + n) % 2 == 1:
                    return max(max_left1, max_left2)
                # If the total number of elements is even
                else:
                    return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2.0
            # If we are too far to the right in nums1, move left
            elif max_left1 > min_right2:
                right = partition1 - 1
            # If we are too far to the left in nums1, move right
            else:
                left = partition1 + 1
        # If input is invalid or arrays are not sorted
        raise ValueError("Input arrays are not sorted or invalid.")