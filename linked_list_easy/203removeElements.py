# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        go=ListNode(-1)
        go.next=head
        cur=go
        while cur:
            while cur.next and cur.next.val==val:
                cur.next=cur.next.next
            cur=cur.next
        return go.next
