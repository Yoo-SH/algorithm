def isSafe(row, col, board, leftUpperDia, leftLowerDia):  # promising
    # 현재 열 이전의 동일 행 검사
    for i in range(col):
        if board[row][i] == 1:
            return False

    # 대각선 상태 검사
    if leftUpperDia[row - col] or leftLowerDia[row + col]:
        return False

    return True


def countQueenByBacktrackingWithRequersive(board, currentY, leftUpperDia, leftLowerDia):
    if currentY >= len(board):  # 모든 퀸을 배치 완료
        return 1

    count = 0
    for i in range(len(board)):  # 각 행에 대해 시도
        if isSafe(i, currentY, board, leftUpperDia, leftLowerDia):  # pruning
            board[i][currentY] = 1  # 퀸 배치
            leftUpperDia[i - currentY] = 1  # 대각선 상태 갱신
            leftLowerDia[i + currentY] = 1  # 대각선 상태 갱신

            count += countQueenByBacktrackingWithRequersive(
                board, currentY + 1, leftUpperDia, leftLowerDia
            )

            board[i][currentY] = 0  # 초기화(하나의 인스턴스 이므로)
            leftUpperDia[i - currentY] = 0  # 대각선 상태 초기화
            leftLowerDia[i + currentY] = 0  # 대각선 상태 초기화

    return count  # 후위 순회


if __name__ == "__main__":
    N = int(input())  # 보드 크기 입력

    board = [[0] * N for _ in range(N)]  # N x N 보드 초기화
    leftUpperDia = [0] * (2 * N)  # 왼쪽 위 대각선 상태
    leftLowerDia = [0] * (2 * N)  # 왼쪽 아래 대각선 상태
    result = countQueenByBacktrackingWithRequersive(
        board, 0, leftUpperDia, leftLowerDia
    )
    print(result)
