# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ret = head
        pos_head = 1
        # mvoe head forward until end of ll
        while head is not None:
            head = head.next
            # only move the return node forward every time the head is
            #   at an even position
            if pos_head % 2 == 0:
                ret = ret.next
            pos_head += 1
        return ret
