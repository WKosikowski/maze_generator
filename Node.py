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


    # def setUpNode(self, node):
    #     self.upNode = node
    #
    # def setDownNode(self, node):
    #     self.downNode = node
    #
    # def setLeftNode(self, node):
    #     self.leftNode = node
    #
    # def setRightNode(self, node):
    #     self.rightNode = node

    def __str__(self):
        return '(' + f'{self.posX}' + ',' + f'{self.posY}' + ')'