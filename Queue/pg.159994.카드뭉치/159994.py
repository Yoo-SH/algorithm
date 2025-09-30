def solution(cards1 : list, cards2 : list, goal: list):
    
    for index, value in enumerate(goal):

        if cards1 and value == cards1[0]:
            cards1.pop(0)
        elif cards2 and value == cards2[0]:
            cards2.pop(0)
        else:
            return "No"


    return "Yes"