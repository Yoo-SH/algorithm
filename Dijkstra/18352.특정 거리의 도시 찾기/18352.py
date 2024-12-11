import sys
import heapq
input = sys.stdin.readline

def zeroGraph(v: int) -> dict:
    return {i: {} for i in range(1, v+1)}

# 간선 추가 함수: 주어진 간선을 받아 인접 리스트에 추가 (방향 그래프)
def initGraph(graph: dict, edges: list):
    for m, n in edges:
        graph[m][n] = 1  # {m : [n: 가중치] } 형태로 저장

def dijkstra_one(graph, start):
    distances = {node: float('inf') for node in graph  } #distances는 각 노드까지의 거리를 저장하는 딕셔너리
    distances[start] = 0 

    priority_queue = [(0, start)] # (거리, 노드)


    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue) # 힙을 사용하여, 대기 중인 노드 중 거리가 가장 짧은 노드 선택

        if distances[current_node] < current_distance:
            continue

        # 선택된 노드의 인접한 노드와의 거리를 계산 및 업데이트 과정
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight # 현재 노드까지의 거리 + 인접한 노드까지의 거리

            # 만약 인접한 노드까지의 거리가 더 짧다면 업데이트(초기에는 무한대로 설정했으므로, 인접한 노드 거리가 업데이트됨)
            if distance < distances[neighbor]: 
                distances[neighbor] = distance
                heapq.heappush(priority_queue, [distance, neighbor])  # 인접한 노드까지의 거리가 업데이트 되었기 때문에 우선순위 큐에 추가
                

    return distances


if __name__ == "__main__":

    N, M, K, X = map(int,input().split())

    edgeRepository: list = []

    for _ in range(M):
        u, v = map(int, input().split())
        edgeRepository.append((u, v)) # u-v

    graph = zeroGraph(N)
    initGraph(graph, edgeRepository)
    distances = dijkstra_one(graph,X)

    resultList = []
    for v, len in distances.items(): #.items() 메소드는 딕셔너리의 키-값 쌍을 튜플로 반환
        if len == K:
            resultList.append(v)
    
    resultList.sort()
    if resultList:
        for v in resultList:
            print(v)
    else:
        print(-1)
