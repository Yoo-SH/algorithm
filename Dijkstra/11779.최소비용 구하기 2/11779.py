import heapq


def zeroGraph(v: int) -> list:
    return [[] for _ in range(v + 1)]


def initGraph(graph: list, startNode: int, endNode: int, value: int):
    graph[startNode].append((endNode, value))


def dijkstra_one_with_path(graph, start, V):
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
    n = int(input())
    m = int(input())

    graph = zeroGraph(n)
    for _ in range(m):
        fromNode, toNode, value = map(int, input().split())
        initGraph(graph, fromNode, toNode, value)

    startNode, endNode = map(int, input().split())
    distance, path = dijkstra_one_with_path(graph, startNode, n)

    print(distance[endNode])
    print(len(path[endNode]))
    print(" ".join(map(str, path[endNode])))
