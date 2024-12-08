import heapq


def zeroGraph(v: int) -> list:
    return [[] for _ in range(v + 1)]


def initGraph(graph: list, startNode: int, endNode: int, value: int):
    graph[startNode].append((endNode, value))


def dijkstra_one(graph, start, V):
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


if __name__ == "__main__":
    # 입력 처리
    V, E = map(int, input().split())
    K = int(input())

    graph = zeroGraph(V)
    for _ in range(E):
        u, v, w = map(int, input().split())
        initGraph(graph, u, v, w)

    result = dijkstra_one(graph, K, V)
    for i in range(1, V + 1):
        if result[i] == float("inf"):
            print("INF")
        else:
            print(result[i])
