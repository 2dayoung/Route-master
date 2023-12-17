import math



distance =[4212, 3801, 4627, 3815, 4255, 845, 415, 976, 462, 1035, 898, 663, 1311, 798, 959]
_time = [623.9, 580.779, 637.147, 527.384, 625.819, 181.2, 106.035, 147.864, 88.206, 213.552, 197.802, 179.596, 168.968, 164.718, 197.987]
address_list = ["충청북도 청주시 흥덕구 사운로 375",
                "충청북도 청주시 서원구 사창동 367-7",
                "충청북도 청주시 서원구 1순환로680번길 13-11",
                "충청북도 청주시 서원구 모충로3번길 26",
                "충청북도 청주시 서원구 내수동로 140",
                "충청북도 청주시 서원구 창직로31번길 12-1"]

# 인접행렬 생성
num_addresses = len(address_list) + 1
adjacency_matrix = [[-1] * num_addresses for _ in range(num_addresses)]
k=0
for i in range(len(address_list)):
    for j in range(i, len(address_list)):
        print(i,"  ",j)
        if i != j:
            adjacency_matrix[i+1][j+1] = distance[k]
            adjacency_matrix[j+1][i+1] = distance[k]  # 무방향 그래프이므로 대칭
            k+=1
        else :
            adjacency_matrix[i+1][j+1] = 0
            

print("인접행렬:")
for row in adjacency_matrix:
    print(row)

