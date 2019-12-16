def find_meeting_point(coordinates):
	x_sum = 0
	y_sum = 0

	n = float(len(coordinates))

	for coordinate in coordinates:
		x_sum += coordinate[0]
		y_sum += coordinate[1]

	x_ave = x_sum/n
	y_ave = y_sum/n

	x = round(x_ave)
	y = round(y_ave)
	
	return (x,y)

find_meeting_point([(0, 0), (3, 1), (2, 2), (4, 4), (0, 5)])
