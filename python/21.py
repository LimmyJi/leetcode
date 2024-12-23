class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        # now we can assume both lists have an element in them
        ans = None
        # get new head
        if list1.val <= list2.val:
            ans = list1
            list1 = list1.next
            ans.next = None
        else:
            ans = list2
            list2 = list2.next
            ans.next = None
        ans_head = ans
        # go thru both lls at the same time, adding the head node
        #   will smaller value out of the 2 to ans
        #   keep going until one of the lists is empty
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                ans.next = list1
                list1 = list1.next
                ans = ans.next
                ans.next = None
            else:
                ans.next = list2
                list2 = list2.next
                ans = ans.next
                ans.next = None
        # if one of the lists is empty, append the rest of the other to ans
        if list1 is None:
            ans.next = list2
        if list2 is None:
            ans.next = list1
        return ans_head
