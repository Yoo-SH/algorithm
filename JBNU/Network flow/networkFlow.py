from collections import defaultdict

# 그래프를 나타내는 클래스 정의
class Graph:
    def __init__(self, vertices):
        # 그래프를 표현하기 위해 defaultdict를 사용
        # 각 정점에 연결된 간선의 리스트를 저장
        self.graph = defaultdict(list)
        # 정점의 총 개수
        self.ROW = vertices

    # 간선을 추가하는 함수 정의
    # u: 출발 정점, v: 도착 정점, w: 간선의 용량(가중치)
    def add_edge(self, u, v, w):
        # 정점 u에서 v로 가는 용량이 w인 간선 추가
        self.graph[u].append([v, w])
        # 역방향 간선을 추가하여, 초기 용량을 0으로 설정 (나중에 유량이 역류할 때 사용)
        self.graph[v].append([u, 0])

    # BFS(너비 우선 탐색)를 사용하여 source에서 sink로 가는 경로가 존재하는지 확인하는 함수
    # s: 시작 정점, t: 목표 정점, parent: 경로를 저장할 리스트
    def bfs(self, s, t, parent):
        # 모든 정점을 방문하지 않은 상태로 초기화
        visited = [False] * self.ROW
        # BFS를 위한 큐 생성
        queue = []
        # 시작 정점을 큐에 추가하고 방문 표시
        queue.append(s)
        visited[s] = True

        # 큐가 빌 때까지 반복
        while queue:
            # 큐의 첫 번째 요소 제거 (FIFO)
            u = queue.pop(0)

            # 현재 정점 u에서 인접한 모든 정점 탐색
            for ind, val in enumerate(self.graph[u]):
                v, w = val
                # 정점 v를 아직 방문하지 않았고 간선의 잔여 용량이 0보다 크면
                if visited[v] == False and w > 0:
                    # 큐에 정점 v 추가
                    queue.append(v)
                    # 정점 v를 방문으로 표시
                    visited[v] = True
                    # 현재 경로에서 v의 부모를 u로 설정 (경로 기록)
                    parent[v] = u

        # 목표 정점 t에 도달했는지 여부 반환
        return True if visited[t] else False

    # 포드-풀커슨 알고리즘을 사용하여 최대 유량을 찾는 함수
    # source: 출발 정점, sink: 목표 정점
    def ford_fulkerson(self, source, sink):
        # 경로를 추적하기 위해 부모 정보를 저장하는 리스트 초기화
        parent = [-1] * self.ROW
        # 최대 유량을 0으로 초기화
        max_flow = 0

        # source에서 sink로 가는 경로가 더 이상 존재하지 않을 때까지 반복
        while self.bfs(source, sink, parent):
            # 현재 경로에서의 최소 용량을 무한대로 초기화
            path_flow = float("Inf")
            s = sink

            # sink에서 source로 거슬러 올라가며 최소 용량을 찾음
            while s != source:
                # 부모 정점에서 현재 정점으로의 간선 용량을 찾음
                for v, w in self.graph[parent[s]]:
                    if v == s:
                        # 현재 경로의 최소 용량을 갱신
                        path_flow = min(path_flow, w)
                # 다음 정점으로 이동 (부모 정점)
                s = parent[s]

            # 경로를 따라 각 간선의 용량을 업데이트 (순방향 및 역방향)
            v = sink
            while v != source:
                u = parent[v]
                # 순방향 간선의 용량 감소
                for i, val in enumerate(self.graph[u]):
                    if val[0] == v:
                        self.graph[u][i][1] -= path_flow
                # 역방향 간선의 용량 증가
                for i, val in enumerate(self.graph[v]):
                    if val[0] == u:
                        self.graph[v][i][1] += path_flow
                # 다음 정점으로 이동 (부모 정점)
                v = parent[v]

            # 현재 경로의 유량을 최대 유량에 추가
            max_flow += path_flow

        # 모든 가능한 경로를 고려한 후 최대 유량 반환
        return max_flow

# 예제 사용법:
g = Graph(6)  # 6개의 정점을 가지는 그래프 생성
g.add_edge(0, 1, 16)  # 정점 0에서 정점 1로 용량 16의 간선 추가
g.add_edge(0, 2, 13)  # 정점 0에서 정점 2로 용량 13의 간선 추가
g.add_edge(1, 2, 10)  # 정점 1에서 정점 2로 용량 10의 간선 추가
g.add_edge(1, 3, 12)  # 정점 1에서 정점 3으로 용량 12의 간선 추가
g.add_edge(2, 1, 4)   # 정점 2에서 정점 1로 용량 4의 간선 추가 (역방향)
g.add_edge(2, 4, 14)  # 정점 2에서 정점 4로 용량 14의 간선 추가
g.add_edge(3, 2, 9)   # 정점 3에서 정점 2로 용량 9의 간선 추가 (역방향)
g.add_edge(3, 5, 20)  # 정점 3에서 정점 5로 용량 20의 간선 추가
g.add_edge(4, 3, 7)   # 정점 4에서 정점 3으로 용량 7의 간선 추가 (역방향)
g.add_edge(4, 5, 4)   # 정점 4에서 정점 5로 용량 4의 간선 추가

source = 0  # 시작 정점 설정
sink = 5    # 목표 정점 설정

# 최대 유량 계산 및 출력
print("최대 유량은  %d" % g.ford_fulkerson(source, sink))
