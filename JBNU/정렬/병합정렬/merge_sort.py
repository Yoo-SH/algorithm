# 병합 정렬
def merge_sort(arr) -> list:
    right = len(arr) - 1
    left = 0
    return merge_sort(arr, left, right)
    

## 병합 정렬을 위한 부가적인 함수
def merge_sort(arr : list , left : int , right :int ) -> None:
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid+1, right)
        merge(arr, left, mid, right)   


## 병합 정렬을 위한 병합 함수
def merge(arr : list, left : int, mid : int, right : int) -> list:
    i = left
    j = mid + 1
    k = left
    merge_arr = [0 for _ in range(len(arr))] # 임시로 값을 저장할 배열


    while i <= mid and j <= right: # 왼쪽과 오른쪽을 비교하여 작은 값을 temp에 넣어줌
        if list[i] <= list[j]:
            merge_arr[k] = list[i]
            i += 1
        else:
            merge_arr[k] = list[j]
            j += 1
        k += 1

    if i > mid: # 왼쪽이 먼저 끝난 경우
        for l in range(j, right + 1):
            merge_arr[k] = list[l]
            k += 1
    else: # 오른쪽이 먼저 끝난 경우
        for l in range(i, mid + 1):
            merge_arr[k] = list[l]
            k += 1

    for l in range(left, right + 1): # temp에 있는 값을 list에 넣어줌
        list[l] = merge_arr[l]
    
    return list
