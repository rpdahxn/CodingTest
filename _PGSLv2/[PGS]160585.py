def solution(board):
    
    o_ = x_ = 0
    for b in board:
        o_ += b.count('O')
        x_ += b.count('X')
        
    if o_ + x_ == 0:
        return 1
    if abs(o_ - x_) > 1 or o_ < x_:
        return 0
    
    o_3 = x_3 = False
    for i in range(3):
        # 가로
        if [board[i][0], board[i][1], board[i][2]] == ['O', 'O', 'O']:
            o_3 = True
        elif [board[i][0], board[i][1], board[i][2]] == ['X', 'X', 'X']:
            x_3 = True
            
        # 세로
        if [board[0][i], board[1][i], board[2][i]] == ['O', 'O', 'O']:
            o_3 = True
        elif [board[0][i], board[1][i], board[2][i]] == ['X', 'X', 'X']:
            x_3 = True
            
        
        if i == 1:
            # 좌-우 대각선
            if [board[0][0], board[1][1], board[2][2]] == ['O', 'O', 'O']:
                o_3 = True
            elif [board[0][0], board[1][1], board[2][2]] == ['X', 'X', 'X']:
                x_3 = True
            # 우-좌 대각선
            if [board[0][2], board[1][1], board[2][0]] == ['O', 'O', 'O']:
                o_3 = True
            elif [board[0][2], board[1][1], board[2][0]] == ['X', 'X', 'X']:
                x_3 = True
    
    if o_3 and x_3:
        return 0
    if o_3 and o_ != x_ +1:
        return 0
    if x_3 and x_ != o_:
        return 0
    
    return 1