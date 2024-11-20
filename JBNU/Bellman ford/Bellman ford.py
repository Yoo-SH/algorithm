def bellman_ford(start):
    # 시작 노드에 대해서 초기화
    distances[start] = 0

    # 전체 v-1번의 라운드(round)를 반복
    for i in range(v):
        # 매 반복마다 "모든 간선"을 확인하며
        for j in range(e):
            cur_node = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]

            # 현재 간선을 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우
            if distances[cur_node] != float("inf") and distances[next_node] > distances[cur_node] + cost:
                distances[next_node] = distances[cur_node] + cost
                # V - 1번째 라운드에서 값이 갱신되는 것을 확인하는 것은 곧 음수 순환이 존재하는지 확인하는 과정
                # v개 노드라면 최대 v-1개의 간선과, 릴랙싱을 하기 때문에 v-1번째 라운드에서 값이 갱신되는 것을 확인하는 것은 곧 음수 순환이 존재하는지 확인하는 과정
                if i == v - 1:
                    return True
    return False


if __name__ == "__main__":
    v, e = map(int, input().split())  # 노드의 개수, 간선의 개수
    
    # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
    edges = []

    # 최단 거리 테이블을 모두 무한으로 초기화
    distances = [float("inf")] * (v + 1) # 1번부터 시작, 0번은 비워둘거임 distances[1]은 1번노드

    # 모든 간선 정보를 입력받기
    for _ in range(e):
        cur_node, next_node, cost = map(int, input().split())
        edges.append((cur_node, next_node, cost))

    # 벨만 포드 알고리즘을 수행
    negative_cycle = bellman_ford(start=1)  # 음수 순환이 발생하는지 확인

    # 음수 순환이 발생할 경우 -1 출력
    if negative_cycle:
        print("-1")
    # 음수 순환이 발생하지 않을 경우 최단 거리 출력
    else:
        for i in range(2, v + 1):
            # 도달할 수 없는 경우, -1 출력
            if distances[i] == float('inf'):
                print("-1")
            # 도달할 수 있는 경우 거리 출력
            else:
                print(distances[i])