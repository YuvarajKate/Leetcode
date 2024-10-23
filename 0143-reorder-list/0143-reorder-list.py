# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        
        # Step 1: Find the middle of the list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # Step 2: Reverse the second half of the list
        prev = None
        current = slow
        while current:
            next_temp = current.next  # Store next node
            current.next = prev       # Reverse the link
            prev = current            # Move prev forward
            current = next_temp       # Move current forward
        
        # Step 3: Merge the two halves
        first, second = head, prev  # First half is head, second half is reversed
        while second.next:  # We stop when we reach the end of the second half
            # Save the next nodes
            tmp1 = first.next
            tmp2 = second.next
            
            # Rearrange the pointers
            first.next = second
            second.next = tmp1
            
            # Move the pointers forward
            first = tmp1
            second = tmp2