def generateParenthesis(self, n: int) -> List[str]:
    result = []
    stack = []
    def generateParenthesisHelper(openN: int, closedN: int):
        if closedN == openN == n:
            result.append("".join(stack))
        if openN < n:
            stack.append("(")
            generateParenthesisHelper(openN+1,closedN)
            stack.pop()
        if closedN < openN:
            stack.append(")")
            generateParenthesisHelper(openN,closedN+1)
            stack.pop()
    generateParenthesisHelper(0,0)
    return result