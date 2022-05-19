import numpy as np
from  setting import *

# 获取可下位置
def init_position(board):
    position=[[x, y] for x, y in zip(np.where(board == 0)[0], np.where(board == 0)[1])]
    return position

# 判断输赢
def is_terminal(board):
    rowsum = np.sum(board, 0)
    colsum = np.sum(board, 1)
    diag_sum_tl = board.trace()
    diag_sum_tr = board[::-1].trace()
    if any(rowsum == board.shape[0]) or any(colsum == board.shape[0]) or diag_sum_tl == board.shape[0] or diag_sum_tr == board.shape[0]:
        return FAIL_VALUE
    elif any(rowsum == -board.shape[0]) or any(colsum == -board.shape[0]) or diag_sum_tl == -board.shape[0] or diag_sum_tr == -board.shape[0]:
        return WIN_VALUE
    elif np.all(board != 0):
        return 0.
    else:
        return None

# 判断谁行走
def action(board):
    if len(board[board!=0])%2==0:
        return AI
    return PEOPLE

if __name__ == '__main__':
    x=np.zeros([3,3])
    print(init_position(x))