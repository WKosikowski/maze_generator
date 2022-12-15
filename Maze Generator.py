
import random
from Node import Node
# from Maze import Maze
# XBOUND = 10
# YBOUND = 10
# STARTY = 0
# STARTX = 0
#
#
# maze = Maze(YBOUND, XBOUND, STARTY, STARTX)
# maze.generate()
# print(maze.maze)

#  -----------------------------------------------------------------------------------------------------------------------
# ========================================================================================================================



# xBound = XBOUND
# yBound = YBOUND
#
# maze = []
#
# for y in range(0,yBound):
# 	row = []
# 	for x in range(0,xBound):
# 		row.append(Node(y, x))
# 	maze.append(row)
#
# maze[STARTY][STARTX].visited = True
# print(maze)
#
# def randomise(y, x):
#
# 	randList: [Node] = []
# 	if x > 0:
# 		if maze[y][x - 1].visited == False:
# 			randList.append("Left")
#
# 	if y > 0:
# 		if maze[y - 1][x].visited == False:
# 			randList.append("Up")
#
# 	if x + 1 < xBound:
# 		if maze[y][x + 1].visited == False:
# 			randList.append("Right")
#
# 	if y + 1 < yBound:
# 		if maze[y + 1][x].visited == False:
# 			randList.append("Down")
#
# 	if len(randList) == 1:
# 		return randList[0]
# 	elif len(randList) > 1:
# 		randNum = random.randint(0, len(randList) - 1)
#
# 		returning = randList[randNum]
# 		return returning
# 	else:
# 		return "null"
#
#
#
#
# def goToNode(direction, yOrigin, xOrigin):
# 	if direction == "Right":
# 		maze[yOrigin][xOrigin].setRightNode(maze[yOrigin][xOrigin + 1])
# 		maze[yOrigin][xOrigin + 1].setLeftNode(maze[yOrigin][xOrigin])
# 		print("movedTo " + "Right")
# 	if direction == "Left":
# 		maze[yOrigin][xOrigin].setLeftNode(maze[yOrigin][xOrigin - 1])
# 		maze[yOrigin][xOrigin - 1].setRightNode(maze[yOrigin][xOrigin])
# 		print("movedTo " + "Left")
# 	if direction == "Down":
# 		maze[yOrigin][xOrigin].setDownNode(maze[yOrigin + 1][xOrigin])
# 		maze[yOrigin + 1][xOrigin].setUpNode(maze[yOrigin][xOrigin])
# 		print("movedTo " + "Down")
# 	if direction == "Up":
# 		maze[yOrigin][xOrigin].setUpNode(maze[yOrigin - 1][xOrigin])
# 		maze[yOrigin - 1][xOrigin].setDownNode(maze[yOrigin][xOrigin])
# 		print("movedTo " + "Up")
#
#
#
# history: [Node] = []
# history.append(maze[STARTY][STARTX])
#
# generationsLeft = (yBound) * (xBound)
#
# i = 0
# while len(history) > 0:
# 	current = history[len(history) - 1]
# 	currentY = current.posY
# 	currentX = current.posX
# 	i = i + 1
# 	print(i, currentX, currentY)
# 	direction = randomise(currentY, currentX)
# 	if direction != "null":
# 		goToNode(direction, currentY, currentX)
# 		if direction == "Up":
# 			currentY -= 1
# 		elif direction == "Left":
# 			currentX -= 1
# 		elif direction == "Down":
# 			currentY += 1
# 		elif direction == "Right":
# 			currentX += 1
# 		maze[currentY][currentX].visited = True
# 		history.append(maze[currentY][currentX])
# 	else:
# 		if len(history) > 0:
# 			del history[len(history) -1]



					

			
			
			
