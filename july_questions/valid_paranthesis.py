def valid_paranthesis(nums):
    stack = []
    pairs = {
    ')': '(',
    ']': '[',
    '}': '{'
    }

    for i in nums:
        if i in "([{":
            stack.append(i)

        else:
            if not stack:
                return False

            if stack[-1] != pairs[i]:
                return False

            stack.pop()

    return not stack

print(valid_paranthesis("()"))
print(valid_paranthesis("()[]{}"))
print(valid_paranthesis("(]"))
print(valid_paranthesis("([)]"))
print(valid_paranthesis("{[]}"))
