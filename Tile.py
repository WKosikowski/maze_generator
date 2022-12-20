class Tile:
    def __init__(self, y, x):
        self.visited = False
        self.neighbourNodesVisited = 0
        self.posX = x
        self.posY = y
        self.upNode = None
        self.rightNode = None
        self.leftNode = None
        self.downNode = None


    def get_neighbours(self, tile):
        if tile.upNode is not None:
            if tile.upNode.visited:
                tile.upNode.visited = False
                return tile.upNode
        if tile.downNode is not None:
            if tile.downNode.visited:
                tile.downNode.visited = False
                return tile.downNode
        if tile.rightNode is not None:
            if tile.rightNode.visited:
                tile.rightNode.visited = False
                return tile.rightNode
        if tile.leftNode is not None:
            if tile.leftNode.visited:
                tile.leftNode.visited = False
                return tile.leftNode
        return None

    def __str__(self):
        return '(' + f'{self.posX}' + ',' + f'{self.posY}' + ' ' + f'{self.rightNode is not None}' + ' ' + f'{self.downNode is not None}' + ')'