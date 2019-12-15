class Board():
	def __init__(self):
		self.reset_board()

	def reset_board(self):
		self.board = [[0 for y in range(3)] for x in range(3)]

	def player_move(self, x, y, player):
		self.board[y][x] = player

		count = 0
		for ix in range(3):
			if self.board[y][ix] == player:
				count += 1
			else:
				break
		if count == 3:
			return 1

		count = 0
		for iy in range(3):
			if self.board[iy][x] == player:
				count += 1
			else:
				break
		if count == 3:
			return 1

		count_1 = 0
		count_2 = 0
		for i in range(3):
			if self.board[i][i] == player:
				count_1 += 1
			if self.board[i][2-i] == player:
				count_2 += 1
		if count_1 == 3 or count_2 == 3:
			return 1
		
		for ix in range(3):
			for iy in range(3):
				if self.board[iy][ix] == 0:
					return 0
		
		return -1