def	is_plusone_dictionary(d):
	for ele in d:
		if ele + 1 != d[ele]:
			return (False)
	return (True)

di = {1:2,3:10,5:6,7:8}

print(is_plusone_dictionary(di))