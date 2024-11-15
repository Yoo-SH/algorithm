import heapq

# 다익스트라 알고리즘, 특정 노드에서 다른 노드까지의 최단 거리를 구하는 경우
def dijkstra_one(graph, start):
    # 1.초기화 단계
    # 1.1 시작 노드의 거리를 0으로 설정하고,나머지 모든 노드의 거리를 무한대로 초기화함
    # 1.2 최단 거리가 확정되지 않은 노드를 관리하기 위한 우선순위 큐를 사용함
    distances = {node: float('inf') for node in graph  } #distances는 각 노드까지의 거리를 저장하는 딕셔너리
    pre_node = {node: None for node in graph} # 직전 노드를 기록하는 딕셔너리
    distances[start] = 0 
    pre_node[start] = start # 시작 노드의 직전 노드는 자기 자신

    # 우선순위 큐를 생성하고, 시작 노드를 추가
    # 최단 거리가 확정되지 않은 노드들.
    priority_queue = [(0, start)] # (거리, 노드)


    while priority_queue:
        # 2.가장 짧은 거리의 노드 선택
        # 2.1 현재 방문하지 않은 노드 중에서 최단 거리가 가장 작은 노드를 선택함
        current_distance, current_node = heapq.heappop(priority_queue)

        # 현재 노드까지의 거리가 이미 계산된 거리보다 크다면 무시(거리가 짧아야 갱신)
        # distances[current_node]는 기존에 계산된 거리.
        if distances[current_node] < current_distance:
            continue

        # 선택된 노드의 인접한 노드와의 거리를 계산 및 업데이트 과정
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight # 현재 노드까지의 거리 + 인접한 노드까지의 거리

            # 만약 인접한 노드까지의 거리가 더 짧다면 업데이트(초기에는 무한대로 설정했으므로, 인접한 노드 거리가 업데이트됨)
            if distance < distances[neighbor]: 
                distances[neighbor] = distance
                heapq.heappush(priority_queue, [distance, neighbor])  # 인접한 노드까지의 거리가 업데이트 되었기 때문에 우선순위 큐에 추가
                pre_node[neighbor] = current_node

    return distances, pre_node



# 다익스트라 알고리즘, 모든 노드에서 다른 노드까지의 최단 거리를 구하는 경우
def dijkstra_matrix(graph):
    result = [] # 결과를 저장할 리스트, 시작 지점마다 (최소 비용과, 직전노드)를 저장하는 딕셔러니를 튜플로 묶어서 저장

    for start in graph:
        distances = {node: float('inf') for node in graph  } 
        pre_node = {node: None for node in graph} 
        distances[start] = 0 
        pre_node[start] = start 


        priority_queue = [(0, start)] # (거리, 노드)


        while priority_queue:
            
            current_distance, current_node = heapq.heappop(priority_queue)


            if distances[current_node] < current_distance:
                continue


            for neighbor, weight in graph[current_node].items():
                distance = current_distance + weight


                if distance < distances[neighbor]: 
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, [distance, neighbor])
                    pre_node[neighbor] = current_node

        result.append((f"시작노드: {start}", distances, pre_node))
    return result

if __name__ == "__main__":
    
    graph = {
        'A' : {'B': 1, 'C': 4},
        'B' : {'A': 1, 'C': 2, 'D': 5},
        'C' : {'A': 4, 'B': 2, 'D': 1},
        'D' : {'B': 5, 'C': 1}
    }
    



    # A에서 다른 노드까지의 최단 거리
    ##print(dijkstra_one(graph, 'A'))
    result = dijkstra_matrix(graph)
    '''
    for start_node, distances, pre_node in result:
        print(start_node)
        print("최단 거리:", distances)
        print("직전 노드:", pre_node)
    '''

