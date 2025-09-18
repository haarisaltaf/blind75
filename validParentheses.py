def isValid(s):
   """
    :type s: str
    :rtype: bool
    """
    closingTracker = {'}' : '{', ']': '[', ')' : '('}  # handle closing brackets
    stackOpenTracker = []  # track open brackets

    for char in s:
        if char in closingTracker:
            if stackOpenTracker and stackOpenTracker[-1] == closingTracker[char]:
                stackOpenTracker.pop()
            else:
                return False
        else:
            stackOpenTracker.append(char)

    return True if not stackOpenTracker else False


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  # tracks open brackets in s
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
#   if closing bracket, gives open bracket

        for c in s:
            #for every character in string
            if c in closeToOpen:
                # if the character is in hashmap key
                if stack and stack[-1] == closeToOpen[c]:  # if corresponging parenthesios
                    # if the stack has data and the last char in stack is the closing bracket
                    stack.pop()  # remove the closing bracket
                else:  # if the stack is empty or last character in stack is not the opening bracket, return false
                    return False
            else:  # if not a closing bracket, add to stack
                stack.append(c)

        return True if not stack else False # true if empty stack.

# adding every open bracket to stack, if the next char is a closing bracket, remove the open bracket in stack as long as the stack isnt empty, if the stack is empty after going thorugh all of the string, return treu.
