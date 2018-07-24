# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        node = None
        while slow:
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt

        while node and head:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True
