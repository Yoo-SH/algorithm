def check_is_matched(s:str):
    stack_for_parentheses = []

    for c in s:
        if c in "{([":
            stack_for_parentheses.append(c)
        elif c == "}":
            try:
                pop_c = stack_for_parentheses.pop()
                if pop_c != "{":
                    return False
            except IndexError:
                return False
        elif c == ")":
            try:
                pop_c = stack_for_parentheses.pop()
                if pop_c != "(":
                    return False
            except IndexError:
                return False
        elif c == "]":
            try:
                pop_c = stack_for_parentheses.pop()
                if pop_c != "[":
                    return False
            except IndexError:
                return False
    
    # 모든 문자를 다 처리한 후 스택이 비어있는지 확인
    if stack_for_parentheses:
        return False
    else:
        return True
            
    

def rotate_to_right(s:str, x: int):
    # 오른쪽으로 x칸씩 이동
    s = s[-x:] + s[:-x]
    return s

def solution(s):

    count_is_matched = 0                    

    # 회전시키면서 문자열이 맞는지 확인
    for x in range(0,len(s)):
        if check_is_matched(rotate_to_right(s,x)):
            count_is_matched += 1
        
        
    return count_is_matched