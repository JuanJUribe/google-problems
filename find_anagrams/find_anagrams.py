def string_contains_anagram(string_a, string_b): # not able to differentiate subsequence from anagram
	string_a = string_a.lower().replace(' ', '')
	string_b = string_b.lower().replace(' ', '')
	boc_b = set([char for char in string_b])
	for char in boc_b:
		if string_b.count(char) > string_a.count(char):
			return False
	return True


def string_contains_anagram(string_a, string_b): # not able to find anagrams at the end
	start = 0
	for char_a in string_a:
		char_b_i = string_b.find(char_a)
		if start == 0 and char_b_i != -1:
			start = 1
			print(1)
		if start == 1 and char_b_i != -1:
			string_b = string_b.replace(char_a, '', 1)
			print(2)
		elif start == 1 and char_b_i == -1:
			print(3)
			break
	print(string_b)
	if string_b == '':
		return True
	return False