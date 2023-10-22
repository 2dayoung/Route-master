import itertools

# 주어진 인접 행렬
graph = [
    [float('inf'), 845, 441, 976, 462],
    [845, float('inf'), 1035, 898, 663],
    [441, 1035, float('inf'), 1311, 798],
    [976, 898, 1311, float('inf'), 959],
    [462, 663, 798, 959, float('inf')]
]

# 모든 노드의 순서 생성
num_nodes = len(graph)
node_indices = range(num_nodes)
permutations = itertools.permutations(node_indices)

# 초기값 설정
shortest_distance = float('inf')
shortest_path = None

# 모든 순서에 대해 최단 경로 찾기
for perm in permutations:
    total_distance = 0
    prev_node = perm[0]

    for node in perm[1:]:
        total_distance += graph[prev_node][node]
        prev_node = node

    # 마지막 노드에서 출발 노드로 돌아가는 거리 추가
    total_distance += graph[prev_node][perm[0]]

    if total_distance < shortest_distance:
        shortest_distance = total_distance
        shortest_path = perm

# 결과 출력
print(f"최단 거리: {shortest_distance}")
print(f"최단 경로: {shortest_path}")