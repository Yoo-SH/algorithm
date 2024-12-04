# 그래프 초기화 함수: 정점의 개수를 받아 인접 리스트를 생성
def zeroGraph(v : int) -> dict:  
    return {i: [] for i in range(v)}

# 간선 추가 함수: 쭈어진 간선을 받아 인접 리스트에 추가(무방향 그래프)
def initGraph(graph: dict, edges: tuple):
    for m,n in edges: 
        graph[m].append(n)
        graph[n].append(m)

# 그래프 출력 함수: 인접 리스트를 받아 출력
def printGraph(graph : dict):
    for v in graph:
        print(f"{v} : {graph[v]}")


# 재귀를 이용한 DFS 함수
def recursive_dfs(graph: dict, visited: set, node: int) -> None:
    if node not in visited:
        print(node)  # 방문한 노드 출력
        visited.add(node)  # 방문한 노드 저장(중복 방지)
        
        # 현재 노드와 연결된 노드를 모두 재귀적으로 방문
        for linked_node in graph[node]:
            if linked_node not in visited:
                recursive_dfs(graph, visited, linked_node)    
    

    
if __name__ == "__main__":
   
    v = 7
    # 그래프를 이진 트리 형태로 생성
    edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6)]
    graph : dict = zeroGraph(v) # 리스트를 value값으로 가지는 딕셔너리
    initGraph(graph, edges) # 그래프 초기화
    #printGraph(graph ) # 그래프 출력
    visited = set()
    recursive_dfs(graph, visited, node=0)
    

    