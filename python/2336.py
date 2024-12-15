class SmallestInfiniteSet(object):

    def __init__(self):
        """
        index 0 to length(SmallestInfiniteSet) will store numbers in the set, in increasing order
        index 0 will always have smallest number
        any number greater than SmallestInfiniteSet[length(SmallestInfiniteSet) - 1] is also in the set, although not explicitly
        """
        # any int > self.Set[-1] is also in the set
        self.Set = [1]
        

    def popSmallest(self):
        """
        :rtype: int
        """
        # self.Set[0] will always have smallest
        result = self.Set[0]
        if len(self.Set) == 1:
            self.Set.append(result + 1)
        self.Set.pop(0)
        return result
        

    def addBack(self, num):
        """
        :type num: int
        :rtype: None
        """
        # if num is greater than self.Set[-1], it is in the set
        length = len(self.Set)
        if num > self.Set[length - 1]:
            return
        # else see if we can add it in the front
        for i in range (0, length):
            if self.Set[i] == num:
                return
            if self.Set[i] > num:
                self.Set.insert(i, num)
                return

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
