import  random
import numpy as np
from  tool import *
from  setting import *

class Node(): # 每个节点的信息
    def __init__(self,board,parent=None,weizi=None):
        self.parent=parent # 父节点
        self.children=[]   # 里面打算存放所有的子节点

        self.visit=0           # 访问次数默认为0
        self.quality_vale=0    # 节点质量
        self.board = board     # 棋盘

        self.weizi=weizi
        self.position=init_position(self.board)   # 获取棋盘位置

    def node_expand(self):
        ai_position=self.position.pop() # 选择一个位置
        son_board=self.board.copy()
        son_board[ai_position[0],ai_position[1]]=action(son_board)
        son_node=Node(parent=self,board=son_board,weizi=ai_position)
        self.children.append(son_node)
        return son_node

    def best_child(self, c_param=2**0.5):
        choices_weights = [
            (c.quality_vale / (c.visit)) + c_param * np.sqrt((2 * np.log(self.visit) / (c.visit)))
            for c in self.children
        ]
        return self.children[np.argmax(choices_weights)]

    def node_simulation(self):
        next_board=self.board.copy()
        position = init_position(next_board)  # 获取可行位置
        while True:
            # 判断
            if is_terminal(next_board) != None:
                value = is_terminal(next_board)
                return value
            # 随机下子
            if position:
                choice = random.choice(position)
                position.remove(choice)
                next_board[choice[0], choice[1]] = action(next_board)

    # 反向传播 ---> 传入游戏结果
    def backpropagate(self, reduce):
        self.visit += 1
        self.quality_vale += reduce
        if self.parent:
            self.parent.backpropagate(reduce)

    def tree_policy(self):
        current_node = self
        while is_terminal(current_node.board) == None:
            if current_node.position:
                return current_node.node_expand()
            else:
                current_node = current_node.best_child()
                return current_node
        return current_node

