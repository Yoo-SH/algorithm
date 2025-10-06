from collections import Counter

def solution(participant, completion):
    
    completion_dictionary = dict(Counter(completion)) # 특정 인원수를 기록하는 딕셔너리, 동명이인도 카운트
    result : str 

    for part in participant:
        if part not in completion_dictionary or completion_dictionary[part] == 0:
            result = part
        else: 
            completion_dictionary[part] -=1 # 동명이인이 있는 경우를 고려하여 갯수 감소


    return result