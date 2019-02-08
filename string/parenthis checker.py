def isBalanced(s):
    stack = []
    left = '{[('
    right = '}])'
    
    for c in s:
        if c in left or not stack:
            stack.append(c)
        elif stack[len(stack)-1] == left[right.index(c)]:
            stack.pop()
        else:
            return 'not balanced'
    
    if not stack:    
        return 'balanced'
    else:
        return 'not balanced'
        
if __name__ == "__main__":
    t = int(input().strip())
    for a in range(t):
        s = input().strip()
        result = isBalanced(s)
        print (result)