def naive_count_inv(a):
	global inv
	inv = 0
	return count_sort(a)

# Naive implementation.
def count_sort(a):
	global inv
	for i in range(0, len(a)):
		tmp = a[i]
		for j in range(i, len(a)):
			if (tmp > a[j]):
				inv += 1
	
	return inv
