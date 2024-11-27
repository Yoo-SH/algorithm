def initialize_apartment():
    # 1. 아파트 층수 및 호수를 나타내는 15x15 배열 초기화
    arr = [[0] * 15 for _ in range(15)]
    # 2. 0층 1호부터 14호까지 초기화
    for i in range(15):
        arr[0][i] = i
    #. 각 층의 1호부터 14호까지의 사람 수 계산
    for i in range(1, 15):
        for j in range(1, 15):
            arr[i][j] = arr[i - 1][j] + arr[i][j - 1]
    return arr

def get_number_of_residents(arr, floor, room):
    return arr[floor][room]

def main():
    arr = initialize_apartment()
    test_cases = int(input())

    for _ in range(test_cases):
        floor = int(input())
        room = int(input())
        print(get_number_of_residents(arr, floor, room))

if __name__ == "__main__":
    main()
