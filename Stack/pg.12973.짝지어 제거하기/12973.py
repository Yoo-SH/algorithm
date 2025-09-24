def solution(s):

    stack = []

    
    for c in s:
        if  (len(stack) == 0) or (c != stack[-1]): #현재 데이터가 스택에 없거나 stack에 아무런 데이터가 없다면
            stack.append(c)
        else:
            stack_top = stack[-1]
            if stack_top == c: # 스택 최상단 문자와 현재 문자가 같다면
                stack.pop()

    if stack: # 엣지 케이스(문자열 홀수개인 경우, 매칭되는게 없는경우)
        return 0
    
    return 1    