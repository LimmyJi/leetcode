class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # think of this nums as a linked list
        #   0 is the root node and
        #   nums[i] is the node that the i-th node points to
        slow = nums[0]
        fast = nums[0]

        # we have entered a loop if slow == fast, since fast travels the
        #   ll twice as fast, it will eventually meet up with slow again
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break

        # start slow from the root, while fast stays in the loop, these will
        #   intersect at start of the loop (dupe) (can prove mathematically)
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return fast
