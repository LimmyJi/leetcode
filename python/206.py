class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        ret = head
        cur = head.next
        head.next = None  # this is new end
        while cur is not None:
            # make next node point to current node
            # make next node the start of the ll, it is now ret
            temp = cur
            cur = cur.next
            temp.next = ret
            ret = temp
        return ret
