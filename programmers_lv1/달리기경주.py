def solution(players, callings):
    dict_rank = {}
    for idx, i in enumerate(players):
        dict_rank[i] = idx
    
    for i in callings:
        players[dict_rank[i]], players[dict_rank[i]-1] = players[dict_rank[i]-1], players[dict_rank[i]]
        dict_rank[i] -= 1
        dict_rank[players[dict_rank[i]+1]] += 1
    return players