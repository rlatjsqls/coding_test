def find_parent(node, parent):
    if parent[node] != node:
        parent[node] = find_parent(parent[node], parent)
    return parent[node]
    
def union_parent(node1, node2, parent):
    node1 = find_parent(node1, parent)
    node2 = find_parent(node2, parent)
    if node1 < node2:
        parent[node2] = node1
    else:
        parent[node1] = node2

def solution(n, costs):
    answer = 0
    parent = [i for i in range(n)]
    costs = sorted(costs, key = lambda x : x [2])
    
    for node1, node2, cost in costs:
        if find_parent(node1, parent) != find_parent(node2, parent):
            union_parent(node1, node2, parent)
            answer += cost
            
    return answer