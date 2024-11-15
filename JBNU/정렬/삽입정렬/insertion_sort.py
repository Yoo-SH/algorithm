# 삽입 정렬
def insertion_sort(arr) -> None:
    for i in range(1, len(arr)):  # 두 번째 원소부터 시작
        for j in range(i, 0, -1):  # 현재 원소를 정렬된 부분과 비교
            if arr[j] < arr[j-1]:  # 현재 원소가 이전 원소보다 작으면 교환
                arr[j], arr[j-1] = arr[j-1], arr[j] # 튜플로 값을 바꿔줌
            else:
                break  # 교환이 일어나지 않으면 종료 (이미 정렬된 상태)
