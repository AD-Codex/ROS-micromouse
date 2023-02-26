

print("hello")

maze = [
		[ 101,   101,    101,    101,    101,    101,    101,    101,    101,    101,    101,    101,    101,    101,    101,    101,    101 ],
		[ 101,   1  ,    0  ,    2  ,    101,    5  ,    0  ,    6  ,    0  ,    7  ,    0  ,    8  ,    101,    11 ,    101,    14 ,    101 ],
		[ 101,   0  ,    -1 ,    0  ,    -1 ,    0  ,    -1 ,    0  ,    -1 ,    101,    -1 ,    0  ,    -1 ,    0  ,    -1 ,    0  ,    101 ],
		[ 101,   2  ,    101,    3  ,    0  ,    4  ,    101,    7  ,    101,    14 ,    101,    9  ,    0  ,    10 ,    101,    13 ,    101 ],
		[ 101,   0  ,    -1 ,    101,    -1 ,    101,    -1 ,    101,    -1 ,    0  ,    -1 ,    101,    -1 ,    0  ,    -1 ,    0  ,    101 ],
		[ 101,   3  ,    101,    16 ,    0  ,    15 ,    0  ,    14 ,    0  ,    13 ,    0  ,    12 ,    0  ,    11 ,    0  ,    12 ,    101 ],
		[ 101,   0  ,    -1 ,    0  ,    -1 ,    0  ,    -1 ,    101,    -1 ,    101,    -1 ,    101,    -1 ,    101,    -1 ,    0  ,    101 ],
		[ 101,   4  ,    101,    17 ,    101,    16 ,    101,    25 ,    0  ,    24 ,    101,    31 ,    101,    30 ,    0  ,    29 ,    101 ],
		[ 101,   0  ,    -1 ,    0  ,    -1 ,    0  ,    -1 ,    0  ,    -1 ,    0  ,    -1 ,    0  ,    -1 ,    0  ,    -1 ,    0  ,    101 ],
		[ 101,   5  ,    101,    18 ,    101,    17 ,    101,    24 ,    0  ,    23 ,    101,    30 ,    101,    29 ,    0  ,    28 ,    101 ],
		[ 101,   0  ,    -1 ,    0  ,    -1 ,    101,    -1 ,    101,    -1 ,    0  ,    -1 ,    0  ,    -1 ,    101,   -1  ,    0  ,    101 ],
		[ 101,   6  ,    101,    19 ,    0  ,    20 ,    0  ,    21 ,    0  ,    22 ,    101,    29 ,    0  ,    28 ,    0  ,    27 ,    101 ],
		[ 101,   0  ,    -1 ,    0  ,    -1 ,    101,    -1 ,    0  ,    -1 ,    0  ,    -1 ,    101,    -1 ,    101,    -1 ,    0  ,    101 ],
		[ 101,   7  ,    101,    20 ,    101,    31 ,    101,    22 ,    101,    23 ,    0  ,    24 ,    0  ,    25 ,    0  ,    26 ,    101 ],
		[ 101,   0  ,    -1 ,    101,    -1 ,    0  ,    -1 ,    101,    -1 ,    101,    -1 ,    101,    -1 ,    0  ,    -1 ,    0  ,    101 ],
		[ 101,   8  ,    101,    31 ,    0  ,    30 ,    0  ,    29 ,    0  ,    28 ,    0  ,    27 ,    0  ,    26 ,    101,    27 ,    101 ],
		[ 101,   101,    101,    101,    101,    101,    101,    101,    101,    101,    101,    101,    101,    101,    101,    101,    101 ]

]


# x_coord = 15
# y_coord = 5

points = [[5,15]]
ij=1


def currect_coord( y, x ):

	count_points = 0

	global y_coord
	global x_coord
	global operation
	global ij

	count = maze[y][x]

	if ( maze[y +1][x] == 0 and maze[y +2][x] > count+1 ):
		print( "maze[y +1][x] == 0 and maze[y +2][x] > count+1" )
		if ( count_points ==0):
			print( y_coord, x_coord)
			maze[y +2][x] = count +1
			y_coord = y +2
			operation = 1
			count_points = 1
		else:
			points.append([ y, x ])
			ij = ij +1

	if ( maze[y -1][x] == 0 and maze[y -2][x] > count+1 ):
		print("maze[y -1][x] == 0 and maze[y -2][x] > count+1")
		if ( count_points ==0):
			print( y_coord, x_coord)
			maze[y -2][x] = count +1
			y_coord = y -2
			operation = 1
			count_points = 1
		else:
			points.append([ y, x ])
			ij = ij +1

	if ( maze[y][x+1] == 0 and maze[y][x+2] > count+1 ):
		print("maze[y][x+1] == 0 and maze[y][x+2] > count+1")
		if ( count_points ==0):
			print( y_coord, x_coord)
			maze[y][x+2] = count +1
			x_coord = x +2
			operation = 1
			count_points = 1
		else:
			points.append([ y, x ])
			ij = ij +1

	if ( maze[y][x-1] == 0 and maze[y][x-2] > count+1 ):
		print("maze[y][x-1] == 0 and maze[y][x-2] > count+1")
		if ( count_points ==0):
			print( y_coord, x_coord)
			maze[y][x-2] = count +1
			x_coord = x -2
			operation = 1
			count_points = 1
		else:
			points.append([ y, x ])
			ij = ij +1


operation = 1

i =0;

count_operation = 0
while True:
	if ( count_operation >= ij ):
		break

	y_coord = points[count_operation][0]
	x_coord = points[count_operation][1]

	operation = 1
	while ( operation) :
		operation = 0
		currect_coord(y_coord, x_coord)
		print("\n")

	count_operation = count_operation +1



# for i in range(7):
# 	y_coord = points[i][0]
# 	x_coord = points[i][1]

# 	operation = 1
# 	while ( operation) :
# 		operation = 0
# 		currect_coord(y_coord, x_coord)
# 		print("\n")


# operation = 1
# while ( operation) :
# 	operation = 0
# 	currect_coord(y_coord, x_coord)
# 	print("\n")





for i in range(17):
	for j in range(17):
		print(maze[i][j] , end=",\t")

	print()

print(points)


# /////////////////////////////////////////////////////////////// short path ////////////////////////////////////////////

def path_find():
	mid_x = 7
	mid_y = 7

	path =[]

	mid_count = maze[mid_y][mid_x]
	print(mid_count)

	currect_y = mid_y
	currect_x = mid_x
	currect_count = mid_count
	path.append([currect_y,currect_x])

	while ( currect_count > 1 ):

		if ( maze[currect_y +1][currect_x] ==0 and maze[currect_y +2][currect_x] == currect_count -1):
			currect_x = currect_x
			currect_y = currect_y + 2
			currect_count = currect_count -1
			path.append([currect_y,currect_x])
		elif ( maze[currect_y][currect_x +1] ==0 and maze[currect_y][currect_x +2] == currect_count -1):
			currect_x = currect_x +2
			currect_y = currect_y
			currect_count = currect_count -1
			path.append([currect_y,currect_x])
		elif ( maze[currect_y -1][currect_x] ==0 and maze[currect_y -2][currect_x] == currect_count -1):
			currect_x = currect_x
			currect_y = currect_y -2
			currect_count = currect_count -1
			path.append([currect_y,currect_x])
		elif ( maze[currect_y][currect_x -1] ==0 and maze[currect_y][currect_x -2] == currect_count -1):
			currect_x = currect_x -2
			currect_y = currect_y
			currect_count = currect_count -1
			path.append([currect_y,currect_x])

	print(path)

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


path_find()