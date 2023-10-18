import numpy as np

# # 50개의 도시 간의 인접 행렬 예시 (임의의 값 사용)
# num_cities = 20
# np.random.seed(0)
# graph = np.random.randint(100, 1000, size=(num_cities, num_cities))
# np.fill_diagonal(graph, 0)  # 대각선 상의 값은 0으로 설정
graph = [
    [float('inf'), 160.112, 102.311, 181.82, 84.446],
    [160.112, float('inf'), 188.688, 201.359, 186.535],
    [102.311, 188.688, float('inf'), 214.102, 157.644],
    [181.82, 201.359, 214.102, float('inf'), 295.018],
    [84.446, 186.535, 157.644, 295.018, float('inf')]
]


def lin_kernighan(graph):
    num_nodes = len(graph)
    best_tour = None
    best_length = float('inf')

    for start_node in range(num_nodes):
        tour = [start_node]
        unused_nodes = set(range(num_nodes))
        unused_nodes.remove(start_node)
        tour_length = 0

        while unused_nodes:
            current_node = tour[-1]
            min_gain = float('inf')
            next_node = -1

            for node in unused_nodes:
                gain = graph[current_node][node]
                if gain < min_gain:
                    min_gain = gain
                    next_node = node

            tour_length += min_gain
            tour.append(next_node)
            unused_nodes.remove(next_node)

        # Check if the tour is better than the best tour found so far
        if tour_length < best_length:
            best_tour = tour
            best_length = tour_length

    return best_length, best_tour

# Lin-Kernighan 알고리즘을 사용하여 최단 경로 찾기
shortest_length, shortest_tour = lin_kernighan(graph)
print(f"Shortest Length: {shortest_length}")
print(f"Shortest Tour: {shortest_tour}")
