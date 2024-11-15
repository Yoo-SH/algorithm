# 버블 정렬
def bubble_sort(arr) -> None:
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # 튜플로 값을 바꿔줌
