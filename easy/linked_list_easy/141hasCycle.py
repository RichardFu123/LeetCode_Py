class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        walker = head
        runner = head.next
        try:
            while walker!=runner:
                walker = walker.next
                runner = runner.next.next
            return True
        except:
            return False
