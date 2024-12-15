# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if head.next is None:
            return head
        # count nodes in the ll
        count = 0
        list1 = head
        while list1 is not None:
            count += 1
            list1 = list1.next
        # the number of nodes that remain in order
        len1 = count - count // 2
        # traverse until we get to the first node that will be inserted in reverse order
        list1 = head
        while len1 != 1:
            list1 = list1.next
            len1 -= 1
        list2 = list1.next
        list1.next = None  # split this partition from the nodes that will remain in order

        # reverse this partition of the ll
        temp1 = list2.next
        list2.next = None
        while temp1 is not None:
            temp2 = temp1.next
            temp1.next = list2
            list2 = temp1
            temp1 = temp2
        
        # now traverse the partition that remains in order, inserting nodes from the reversed
        #   second partition
        list1 = head
        while list1 is not None and list2 is not None:
            temp1 = list1.next
            temp2 = list2.next
            list2.next = temp1
            list1.next = list2
            list2 = temp2
            list1 = temp1

        return head
        