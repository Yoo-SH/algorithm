from collections import deque

# 상수 정의
OBSTACLE = -1  # 장애물을 의미하는 값
MOVE_Y = [1, -1]  # 위 아래 이동 방향


def is_valid_position(y, x, n):
    """
    삼각형 내부와 경계를 검사합니다.
    Args:
        y (int): 세로 위치
        x (int): 가로 위치
        n (int): 격자의 크기
    Returns:
        bool: 유효한 위치면 True, 아니면 False
    """
    if x <= n:
        return 0 <= y <= x  # 왼쪽 절반 검사
    return 0 <= y <= (2 * n - x)  # 오른쪽 절반 검사


def bfs(start_y, start_x, n, grid, visited, dx):
    """
    BFS를 사용하여 격자 내 이동 가능한 모든 위치를 탐색.
    Args:
        start_y (int): 시작 y 좌표
        start_x (int): 시작 x 좌표
        n (int): 격자의 크기
        grid (list): 장애물과 빈 칸이 있는 격자
        visited (list): 방문 여부를 저장하는 2차원 리스트
        direction (int): 이동하는 가로 방향 (1: 오른쪽, -1: 왼쪽)
    """
    queue = deque([(start_y, start_x)])
    visited[start_y][start_x] = True

    while queue:
        current_y, current_x = queue.popleft()
        for dy in MOVE_Y:
            next_y, next_x = current_y + dy, current_x + dx

            # 범위 검사 및 유효 위치 검사
            if not is_valid_position(next_y, next_x, n):
                continue

            # 방문 여부 및 장애물 검사
            if not visited[next_y][next_x] and grid[next_y][next_x] != OBSTACLE:
                visited[next_y][next_x] = True
                queue.append((next_y, next_x))


def find_max_y(n, visited1, visited2):
    """
    두 BFS 탐색 결과를 기반으로 조건을 만족하는 최대 y 값을 찾음.
    Args:
        n (int): 격자의 크기
        visited1 (list): 첫 번째 BFS 탐색 결과
        visited2 (list): 두 번째 BFS 탐색 결과
    Returns:
        int: 조건을 만족하는 최대 y 값
    """
    return max(
        y
        for y in range(n + 1)
        for x in range(2 * n + 1)
        if visited1[y][x] and visited2[y][x]
    )


def main():
    """프로그램 실행 함수"""

    n, m = map(int, input().split())
    grid = [[0] * (2 * n + 1) for _ in range(n + 1)]
    for _ in range(m):
        x, y = map(int, input().split())
        grid[y][x] = OBSTACLE  # 장애물 표시

    # 방문 여부를 저장하는 배열 초기화
    visited_from_left = [[False] * (2 * n + 1) for _ in range(n + 1)]
    visited_from_right = [[False] * (2 * n + 1) for _ in range(n + 1)]

    # BFS 탐색 수행
    bfs(0, 0, n, grid, visited_from_left, dx=1)  # 왼쪽에서 오른쪽으로 이동
    bfs(0, 2 * n, n, grid, visited_from_right, dx=-1)  # 오른쪽에서 왼쪽으로 이동

    # 결과 계산
    if visited_from_left[0][2 * n] and visited_from_right[0][0]:
        print(find_max_y(n, visited_from_left, visited_from_right))
    else:
        print(-1)


if __name__ == "__main__":
    main()
