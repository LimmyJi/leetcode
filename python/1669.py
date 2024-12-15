# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """
        prev = None
        head = list1
        count = 0
        while count < a:
            prev = head
            head = head.next
            count += 1
        # now head will point to the a-th node
        # prev will point to node before
        while count <= b:
            head = head.next
            count += 1
        # now head will point to the node that the b-th node points to
        prev.next = list2
        while prev.next is not None:
            prev = prev.next
        prev.next = head
        return list1
