def count_inv(a):
	global inv
	inv = 0
	return count_sort(0, len(a) - 1, a)

# Recursive solution.
def count_sort(lower, upper, a):
	global inv
	'''
	Recursive structure:
		-> count_sort (a_left).
		-> count_sort (a_right).
		-> count_split inversions.
	'''
	n = upper - lower + 1;
	
	'Base case:'
	if (n < 2):
		return inv
	elif (n == 2):
		if (a[upper] >= a[lower]):
			return inv
		else:
			inv += 1

			# Swap the two values.
			tmp = a[upper]
			a[upper] = a[lower]
			a[lower] = tmp
			return inv

	#Recursive implementation:
	else:
		count_sort(lower, (lower + upper) / 2, a)
		count_sort((lower + upper) / 2 + 1, upper, a)
		count_split(lower, upper, a)
		return inv

'''
Count inverions of sorted sub-arrays.
'''
def count_split(lower, upper, a):
	global inv
	left = a[lower : (lower + upper) / 2 + 1]
	right = a[(lower + upper) / 2 + 1 : upper + 1]

	i, j = 0, 0
	
	while ((i < len(left)) & (j < len(right))):
		if (left[i] < right[j]):
			a[lower + i + j] = left[i]
			i += 1
		elif (left[i] > right[j]):
			a[lower + i + j] = right[j]
			inv += len(left) - i;
			j += 1
		else:
			a[lower + i + j] = left[i]
			i += 1
	
	while (i < len(left)):
		a[lower + i + j] = left[i]
		i += 1

	while (j < len(right)):
		a[lower + i + j] = right[j]
		j += 1