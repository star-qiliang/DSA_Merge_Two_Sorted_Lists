# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        if not head.next:
            return head


        cur1 = head
        cur2 = cur1.next
        next_node = cur2.next
        cur2.next = cur1
        cur1.next = next_node
        head = cur2
        pre = cur1

        while next_node:
            cur1 = next_node
            cur2 = cur1.next
            if not cur2:
                return head     
            next_node = cur2.next
            cur2.next = cur1
            cur1.next = next_node

            pre.next = cur2
            pre = cur1


        return head