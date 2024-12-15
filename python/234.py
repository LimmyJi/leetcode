# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    # reverse a linked list, given the head
    # copied from 203.py
    # runs in O(n), uses O(1) space
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

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # count number of nodes in the ll
        count = 1
        temp = head.next
        while temp:
            temp = temp.next
            count += 1
        # 1 node = True
        if count == 1:
            return True
        # get the # of nodes in a half
        half = count / 2
        temp = head
        while half > 1:
            temp = temp.next
            half -= 1
        # if odd # of nodes, move forward once
        if count % 2:
            temp = temp.next
        # reverse the second half
        temp.next = self.reverseList(temp.next)
        temp = temp.next
        # check if first half matches second half
        for _ in range(count / 2):
            if head.val != temp.val:
                return False
            head = head.next
            temp = temp.next
        return True
