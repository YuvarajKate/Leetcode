# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Initialize two pointers, slow and fast
        slow, fast = head, head
        
        # Traverse the list with the two pointers
        while fast and fast.next:
            slow = slow.next        # Slow moves one step
            fast = fast.next.next   # Fast moves two steps
            
            # If they meet, there's a cycle
            if slow == fast:
                return True
        
        # If we exit the loop, there's no cycle
        return False