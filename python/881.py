class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        ret = 0
        people.sort()
        left = 0
        right = len(people) - 1
        # pair up the heaviest avail person with lightest, since max of 2 per boat
        while right > left:
            # if both fit, move left to next lightest, right to next heaviest
            if people[left] + people[right] <= limit:
                left += 1
            # else if only 1 fits, put heaviest
            right -= 1
            ret += 1

        # if there is 1 remaining person
        if right == left:
            ret += 1
        return ret
