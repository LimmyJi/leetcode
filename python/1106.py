class Solution(object):
    def parseBoolExpr(self, expression):
        """
        :type expression: str
        :rtype: bool
        """
        # simple True/False
        if expression == "t":
            return True
        if expression == "f":
            return False
        # negation of inner expression
        if expression[0] == "!":
            return not self.parseBoolExpr(expression[2:-1])
        
        # if we come across a & or |, eval inner expression accordingly
        if expression[0] == "&":
            temp = 0  # keeps track of number of '(' found, without a corresponding ')'
            cur = ""  # keeps track of current segment

            for c in expression[2:-1]:
                # if temp != 0, this comma belongs in a pair of inner brackets, add it to cur
                # if temp == 0, dont add the comma to cur, since it is dividing segments
                if c == ",":
                    if temp != 0:
                        cur = cur + c
                else:
                    cur = cur + c
                    if c == "(":
                        temp = temp + 1
                    if c == ")":
                        temp = temp - 1
                    # if temp == 0, we have come to the end of the segment, can evaluate it
                    if (c == "t" or c == "f" or c == ")") and temp == 0:
                        if not self.parseBoolExpr(cur):
                            return False
                        cur = ""
            return True

        # similar logic to '&' case, expecpt diffent True/False logic
        if expression[0] == "|":
            temp = 0
            cur = ""

            for c in expression[2:-1]:
                if c == ",":
                    if temp != 0:
                        cur = cur + c
                else:
                    cur = cur + c
                    if c == "(":
                        temp = temp + 1
                    if c == ")":
                        temp = temp - 1
                    if (c == "t" or c == "f" or c == ")") and temp == 0:
                        if self.parseBoolExpr(cur):
                            return True
                        cur = ""
            return False
