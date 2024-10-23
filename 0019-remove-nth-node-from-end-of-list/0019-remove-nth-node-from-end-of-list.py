# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node to simplify edge cases
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy
        
        # Move fast pointer n + 1 steps ahead
        for _ in range(n + 1):
            fast = fast.next
            
        # Move both pointers until fast reaches the end
        while fast:
            slow = slow.next
            fast = fast.next
            
        # Skip the desired node
        slow.next = slow.next.next
        
        # Return the modified list, which starts from the next of dummy
        return dummy.next