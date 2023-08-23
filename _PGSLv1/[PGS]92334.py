def solution(id_list, report, k):
    
    users = {id:0 for id in id_list}
    result = {id:0 for id in id_list}
    
    report = set(report)
    for r in report:
        user, who = r.split(" ")
        users[who] += 1
        
    for r in report:
        user, who = r.split(" ")
        if users[who] >= k:
            result[user] += 1
            
    return list(result.values())