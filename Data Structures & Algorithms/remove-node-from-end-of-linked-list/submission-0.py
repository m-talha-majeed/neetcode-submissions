# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy= ListNode()
        dummy.next = head
        fast = dummy
        slow=dummy
        for i in range(n): 
            fast= fast.next
        while fast.next!=None:
            fast= fast.next
            slow= slow.next
        temp = slow.next.next
        slow.next = temp
        return dummy.next
                 
        