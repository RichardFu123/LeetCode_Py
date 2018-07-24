class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        p = head
        q = head.next
        while q:
            if q.val == p.val:
                p.next = q.next
                q = q.next
            else:
                p = p.next
                q = q.next
        return head
