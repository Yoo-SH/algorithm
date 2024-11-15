def n_queen(y: int) -> None:
    global cout
    if y == n:
        cout += 1
        return
    for x in range(n):
        if queen_x[x] == "F" and queen_right_upper[x + y] == "F" and queen_right_under[x - y + n - 1] == "F": 
            queen_x[x] = "T"
            queen_right_upper[x + y] = "T"
            queen_right_under[x - y + n - 1] = "T"
            n_queen(y + 1)  # 다음 행으로 이동
            queen_x[x] = "F"
            queen_right_upper[x + y] = "F"
            queen_right_under[x - y + n - 1] = "F"


if __name__ == "__main__":
    n = int(input())
    cout = 0  # 정답 개수를 세는 변수
    queen_x = { i: "F" for i in range(n) }  # 각 열에 퀸이 놓였는지 여부
    queen_right_upper = { i: "F" for i in range(2 * n - 1) }  # 오른쪽 위 대각선
    queen_right_under = { i: "F" for i in range(2 * n - 1) }  # 오른쪽 아래 대각선
    n_queen(0)
    print(cout)
