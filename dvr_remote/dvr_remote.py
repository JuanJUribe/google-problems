import string

class DvrRemote():
	def __init__(self):
		self.abc = string.ascii_lowercase

	def remoteControlSequence(self, input):
		sequence = ''
		p_letter_i = self.abc.find('a')
		for letter in input:
			x_string =''
			y_string =''
			letter_i = self.abc.find(letter)
			difference = letter_i - p_letter_i
			x_move = letter_i%5 - p_letter_i%5
			if x_move>0:
				x_string = ('r'*x_move)
				difference -= x_move
			elif x_move<0:
				x_string += ('l'*-x_move)
				difference -= x_move
			y_move = difference/5
			if y_move>0:
				y_string += ('d'*y_move)
			elif y_move<0:
				y_string += ('u'*-y_move)
			if letter == 'z':
				sequence += (x_string+y_string+'!')
			else:
				sequence += (y_string+x_string+'!')
			p_letter_i = letter_i
		return sequence