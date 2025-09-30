from collections import Counter

def solution(want, number, discount):

    dict_want = dict(zip (want,number))
    sliding_window_len = len(want)
    result = 0

    for i in range(0,len(discount)-sliding_window_len+1):
        slided_discount = dict(Counter(discount[i:i+sliding_window_len]))
        if dict_want == slided_discount:
            result +=1 
    
    return result