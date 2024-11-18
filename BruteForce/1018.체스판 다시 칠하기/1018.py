def count_changes(board, start_x, start_y, first_color):
    #4. 다시 칠해야 하는 최소값을 구한다. (8*8을 순회하며 로직을 만들어 계산)
    # (x+y) % 2 == 0 이 되는 것 끼리는 동일한 색
    # (x+y) % 2 != 0 이 되는 것 끼리는 동일한 색
    changes = 0
    for x in range(8):
        for y in range(8):
            if (x + y) % 2 == 0:
                expected_color = first_color
            else:
                expected_color = 'B' if first_color == 'W' else 'W'
            if board[start_x + x][start_y + y] != expected_color:
                changes += 1
    return changes

if __name__ == "__main__":
  
    #1. N*M크기의 체스판을 만든다
    #2. 체스판의 값 B,W를 입력받아 넣는다.
    N, M = map(int, input().split())
    board = [input() for _ in range(N)]

    min_changes = float('inf')
    #3. 8*8 크기의 체스판을 보드판에서 가져온다.
    #3.1 8*8 크기의 체스판을 만듦.
    for start_x in range(N - 7):
        for start_y in range(M - 7):
            changes_white = count_changes(board, start_x, start_y, 'W')
            changes_black = count_changes(board, start_x, start_y, 'B')
            #5. 보드판 중, 가장 최소 횟수를 구한다.
            min_changes = min(min_changes, changes_white, changes_black)

    print(min_changes)
