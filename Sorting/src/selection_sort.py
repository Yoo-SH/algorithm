# 선택 정렬
def selection_sort(arr) -> None:
    for i in range(len(arr)):
        min_pos : int  = i # 정렬된 인덱스(앞에서부터 최소값을 하나씩 선택하여 정렬) 
        for j in range(min_pos +1, len(arr)):  
            if arr[j] < arr[min_pos]:
                min_pos  = j # 가장 작은 수가 존재하는 인덱스를 찾을 떄마다 갱신

        # 가장 작은 수를 찾아서 ordered_list의 앞에 삽입 (스택처럼 동작)
        arr[i], arr[min_pos ] = arr[min_pos], arr[i] # 튜플로 값을 바꿔줌
