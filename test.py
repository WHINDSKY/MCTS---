import random
import numpy as np
from node import *

def AI_SET(board):
    a = Node(board=board)
    for i in range(1000):
        v = a.tree_policy()
        result = v.node_simulation()
        v.backpropagate(result)
    # for c in a.children:
    #     print((c.quality_vale / (c.visit)) + 2**0.5 * np.sqrt((2 * np.log(c.parent.visit) / (c.visit))),c.weizi)
    return a.best_child(c_param=0).weizi

if __name__ == '__main__':
    ai=0
    people=0
    pen=0
    for i in range(1000):
        # 生成棋盘
        board_set = np.zeros([3, 3])
        # 游戏进行
        while True:
                index = AI_SET(board_set)
                board_set[index[0], index[1]] = -1
                print(board_set)
                if is_terminal(board_set) == WIN_VALUE:  # 判断游戏
                    ai += 1
                    print(ai, people, pen)
                    break
                elif is_terminal(board_set) == FAIL_VALUE:
                    people += 1
                    print(board_set)
                    print(ai, people, pen)
                    break
                elif is_terminal(board_set) == 0:
                    pen += 1
                    print(ai, people, pen)
                    break

                # people_set=[int(i) for i in input('输入下棋位置:').split(',')]
                position = [[x, y] for x, y in zip(np.where(board_set == 0)[0], np.where(board_set == 0)[1])]
                people_set = random.choice(position)
                board_set[people_set[0], people_set[1]] = 1
                print(board_set)
                if is_terminal(board_set) == WIN_VALUE:  # 判断游戏
                    ai += 1
                    print(ai, people, pen)
                    break
                elif is_terminal(board_set) == FAIL_VALUE:
                    people += 1
                    print(board_set)
                    print(ai, people, pen)
                    exit()
                    break
                elif is_terminal(board_set) == 0:
                    pen += 1
                    print(ai, people, pen)
                    break


