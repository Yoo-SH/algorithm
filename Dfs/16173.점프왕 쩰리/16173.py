if __name__ == "__main__":
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]  # 방문한 노드 저장 집합(중복 방지)
    stack = [(0, 0)]  # 시작점 추가
    visited[0][0] = 1  # 시작점 방문 처리

    while stack:
        x, y = stack.pop()
        if matrix[x][y] == -1:
            print("HaruHaru")
            break
        # 오른쪽, 아래쪽으로 이동
        for dx, dy in [(0, matrix[x][y]), (matrix[x][y], 0)]:
            nx, ny = x + dx, y + dy
            if nx < N and ny < N and not visited[nx][ny]:
                stack.append((nx, ny))
                visited[nx][ny] = 1
    else:
        print("Hing")
