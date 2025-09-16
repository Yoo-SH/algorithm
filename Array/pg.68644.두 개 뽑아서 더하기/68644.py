def solution(numbers):

    set_sum = set()
    for index_i, value_i in enumerate(numbers):
        for index_j, value_j in enumerate(numbers):
            if value_i == value_j and index_i == index_j:
                break
            else:
                set_sum.add(value_i + value_j)

    answer = []

    answer = [i for i in set_sum]

    answer.sort()

    return answer
