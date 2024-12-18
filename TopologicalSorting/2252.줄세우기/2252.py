from collections import deque


def topological_sort():
    # 학생 수(N), 비교 횟수(M)
    N, M = map(int, input().split())

    # 그래프 초기화
    graph = [[] for _ in range(N + 1)]
    indegree = [0] * (N + 1)  # 각 노드의 진입 차수

    # 그래프 입력 받기
    for _ in range(M):
        A, B = map(int, input().split())
        graph[A].append(B)
        indegree[B] += 1

    # 진입 차수가 0인 노드를 큐에 삽입
    queue = deque()
    for i in range(1, N + 1):
        if indegree[i] == 0:
            queue.append(i)

    # 위상 정렬 결과 저장
    result = []

    while queue:
        current = queue.popleft()
        result.append(current)

        # 연결된 노드의 진입 차수 감소
        for next_node in graph[current]:
            indegree[next_node] -= 1
            if indegree[next_node] == 0:
                queue.append(next_node)

    # 결과 출력
    print(*result)


if __name__ == "__main__":
    topological_sort()
