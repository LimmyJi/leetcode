class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        length = len(salary)
        # keep track of minimum, maximum and total
        minimum = min(salary[0], salary[1])
        maximum = max(salary[0], salary[1])
        total = 0.0
        for i in range (2, length):
            if salary[i] < minimum:
                total = total + minimum
                minimum = salary[i]
            elif salary[i] > maximum:
                total = total + maximum
                maximum = salary[i]
            else:
                total = total + salary[i]
        # note that maximum and minumum were never added to total
        return total / (length - 2)
            