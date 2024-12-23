class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # outer list is a stack, with the observed brackets
        outer_list = []
        # the corresponding left/right bracket pairs
        bracket_dict = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }
        # go thru the string
        for char in s:
            # add left brackets to the top of stack
            if char in bracket_dict.keys():
                outer_list.append(char)
            else:
                # if we come across a right bracket, try to match it with a left
                #    bracket from the top of the stack 
                if outer_list != [] and bracket_dict[outer_list[-1]] == char:
                    outer_list.pop(-1)
                else:
                    return False
        # no leftovers                
        if outer_list == []:
            return True
        return False
