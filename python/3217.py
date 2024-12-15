# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # tab[i] = nodes with val i
        tab = {}
        temp = head
        while temp:
            if temp.val in tab:
                tab[temp.val].append(temp)
            else:
                tab[temp.val] = [temp]
            temp = temp.next

        # mark nodes for removal
        for num in nums:
            if num in tab:
                for node in tab[num]:
                    node.val = -1
        
        # get new head
        while head.val == -1:
            head = head.next
        # removing marked nodes
        prev = head
        temp = head.next
        while temp:
            if temp.val == -1:
                prev.next = temp.next
            else:
                prev = temp
            temp = temp.next
        return head
