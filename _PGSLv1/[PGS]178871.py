def solution(players, callings):
    
    rank = {player:i for i, player in enumerate(players)}
    for c in callings:
        idx = rank[c]  # 호명된 선수의 지금 등수
        rank[c] -= 1  # 호명된 선수 순위 변경
        rank[players[idx-1]] += 1
        players[idx-1], players[idx] = players[idx], players[idx-1]
        
    return players