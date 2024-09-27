# 힙 정렬
def heap_sort(arr) -> None:
    heap_size = len(arr) # 힙의 크기

    heap_build(arr, heap_size) # 힙을 만들어줌

    for i in range(heap_size - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i) # 힙을 정렬해줌


    pass

def heap_build(unsorted, heap_size):
    for i in range(heap_size // 2, -1, -1):
        heapify(unsorted, i, heap_size)


## 힙 정렬을 위한 부가적인 함수
def heapify(unsorted, index, heap_size):
    

    pass
