class Node:
    def __init__(self, y, x):
        self.visited = False
        self.neighbourNodesVisited = 0
        self.posX = x
        self.posY = y
        self.upNode = None
        self.rightNode = None
        self.leftNode = None
        self.downNode = None



    def __str__(self):
        return '(' + f'{self.posX}' + ',' + f'{self.posY}' + ' ' + f'{self.rightNode is not None}' + ' ' + f'{self.downNode is not None}' + ')'