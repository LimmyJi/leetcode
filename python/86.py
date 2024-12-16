# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        prev = None
        ans = None
        # ans_head will be a ll with all the nodes w/ val < x
        # first_geq will be a ll with all the nodes w/ val geq x
        ans_head = None
        first_geq = None
        # traverse the ll, sorting nodes
        while head is not None:
            # < x, add the node to ans_head, and remove it from the OG ll
            if head.val < x:
                if ans is None:
                    ans = ListNode(head.val)
                    ans_head = ans
                else:
                    ans.next = ListNode(head.val)
                    ans = ans.next
                if prev is not None:
                    prev.next = head.next
            # the first node w/ val geq x will be the head of the first_geq ll, which
            #   is made by deleting all nodes w/ val < x from the OG ll
            else:
                if first_geq is None:
                    first_geq = head
                prev = head
            head = head.next
        # append first_geq to the end of ans_head
        ans = ans_head
        if ans_head is None:
            return first_geq
        else:
            while ans_head.next is not None:
                ans_head = ans_head.next
        ans_head.next = first_geq
        return ans
