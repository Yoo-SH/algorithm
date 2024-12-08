import heapq


def zeroGraph(v: int) -> list:
    """그래프 초기화"""
    return [[] for _ in range(v + 1)]


def initGraph(graph: list, startNode: int, endNode: int, value: int):
    """그래프에 간선 추가"""
    graph[startNode].append((endNode, value))


def dijkstra_one_without_path(graph, start, V):
    """최단 거리만 계산하는 다익스트라 알고리즘"""
    distances = [float("inf")] * (V + 1)
    distances[start] = 0
    priority_queue = [(0, start)]  # (거리, 노드)

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if distances[current_node] < current_distance:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


def dijkstra_one_with_path(graph, start, V):
    """최단 거리와 경로를 기록하는 다익스트라 알고리즘"""
    distances = [float("inf")] * (V + 1)
    pre_node = [None] * (V + 1)
    distances[start] = 0
    pre_node[start] = start
    priority_queue = [(0, start)]  # (거리, 노드)

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if distances[current_node] < current_distance:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                pre_node[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    # 경로 재구성
    paths = reconstruct_paths(pre_node, start, V)
    return distances, paths


def reconstruct_paths(pre_node, start, V):
    """경로 재구성"""
    paths = [[] for _ in range(V + 1)]
    for node in range(1, V + 1):
        current = node
        while current is not None and current != start:
            paths[node].append(current)
            current = pre_node[current]
        if current == start:
            paths[node].append(start)
        paths[node].reverse()  # 시작점에서 도착점 순서로 정렬
    return paths


if __name__ == "__main__":
    # 입력 처리
    V, E = map(int, input("정점 개수와 간선 개수를 입력하세요: ").split())
    K = int(input("시작 정점을 입력하세요: "))

    graph = zeroGraph(V)
    print(f"{E}개의 간선 정보를 입력하세요 (출발 정점, 도착 정점, 가중치):")
    for _ in range(E):
        u, v, w = map(int, input().split())
        initGraph(graph, u, v, w)

    # 최단 거리만 계산
    print("\n최단 거리 결과 (경로 기록 없음):")
    result = dijkstra_one_without_path(graph, K, V)
    for i in range(1, V + 1):
        if result[i] == float("inf"):
            print(f"{i}: INF")
        else:
            print(f"{i}: {result[i]}")

    # 최단 거리 및 경로 계산
    print("\n최단 거리 및 경로 결과 (경로 기록):")
    distances, paths = dijkstra_one_with_path(graph, K, V)
    for i in range(1, V + 1):
        if distances[i] == float("inf"):
            print(f"{i}: INF, 경로: 없음")
        else:
            print(f"{i}: {distances[i]}, 경로: {' -> '.join(map(str, paths[i]))}")
