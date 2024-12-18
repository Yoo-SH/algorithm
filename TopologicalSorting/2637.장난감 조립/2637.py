from collections import deque, defaultdict


def toy_assembly():
    import sys

    input = sys.stdin.read
    data = input().splitlines()

    # 입력 처리
    N = int(data[0])  # 총 부품 수
    M = int(data[1])  # 조립 관계 수
    graph = defaultdict(list)
    in_degree = [0] * (N + 1)
    needs = [[0] * (N + 1) for _ in range(N + 1)]  # 각 부품별 필요한 기본 부품 수

    # 그래프 구축
    for i in range(2, 2 + M):
        X, Y, K = map(int, data[i].split())
        graph[Y].append((X, K))
        in_degree[X] += 1

    # 위상 정렬
    queue = deque()
    for i in range(1, N + 1):
        if in_degree[i] == 0:  # 기본 부품
            queue.append(i)

    while queue:
        current = queue.popleft()
        for next_part, count in graph[current]:
            if sum(needs[current]) == 0:  # 기본 부품인 경우
                needs[next_part][current] += count
            else:  # 중간 부품인 경우
                for i in range(1, N + 1):
                    needs[next_part][i] += needs[current][i] * count
            in_degree[next_part] -= 1
            if in_degree[next_part] == 0:
                queue.append(next_part)

    # 기본 부품 출력
    for i in range(1, N + 1):
        if sum(needs[i]) == 0:  # 기본 부품만 출력
            print(i, needs[N][i])


if __name__ == "__main__":
    toy_assembly()
