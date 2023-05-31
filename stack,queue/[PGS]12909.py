def solution(s):
    stack = list()
    
    for _ in s:
        if _ == ')' and len(stack)>=1 and stack[-1] == '(':
            stack.pop()
        else:
            stack.append(_)
                
    return bool(len(stack)==0)