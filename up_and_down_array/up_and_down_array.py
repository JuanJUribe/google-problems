def find_max_idx(array):
	if len(array) == 0:
		return -1
	sorted_array = list(array)
	sorted_array.sort()
	max_value = sorted_array[-1]
	return array.index(max_value)