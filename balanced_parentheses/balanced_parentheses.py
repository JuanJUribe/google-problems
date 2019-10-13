def is_string_balanced(string):
	if string.count('(') != string.count(')'):
		return False

	while string.find('(') != -1:
		if string.find('(')	> string.find(')'):
			return False
		else:
			string = string.replace('(', '',  1)
			string = string.replace(')', '',  1)
	return True

	