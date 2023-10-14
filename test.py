import math

# 좌표 리스트
distance =[845, 441, 976, 462, 1035, 898, 663, 1311, 798, 959]
_time =[160.112, 102.311, 181.82, 84.446, 188.688, 201.359, 186.535, 214.102, 157.644, 295.018]
address_list = ["충청북도 청주시 서원구 사창동 367-7",
               "충청북도 청주시 서원구 1순환로680번길 13-11",
               "충청북도 청주시 서원구 모충로3번길 26",
               "충청북도 청주시 서원구 내수동로 140",
               "충청북도 청주시 서원구 창직로31번길 12-1"]


# 인접 행렬 초기화 (모든 값을 무한대로 초기화)
adjacency_matrix = [[float('inf')] * len(address_list) for _ in range(len(address_list))]
k=0

for i in range(len(address_list)):
    for j in range(i + 1, len(address_list)):
        
        adjacency_matrix[i][j] = distance[k]
        adjacency_matrix[j][i] = distance[k]  # 무방향 그래프이므로 대칭
        k+=1

# 인접 행렬 출력
for row in adjacency_matrix:
    print(row)
       