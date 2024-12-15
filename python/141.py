# Definition for singly-linked list. 287
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # can also do with fast/slow pointers like we did in 287
        dummy = ListNode()
        dummy.val = 100001
        # traverse the ll, making all nodes point to dummy
        while head is not None:
            # if we find dummy, that means we visited a node that was
            #   already traversed
            if head.val == 100001:
                return True
            next_node = head.next
            head.next = dummy
            head = next_node
        # else if we reach the end, no cycle
        return False
