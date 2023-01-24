def	char_count(str):
	ret = {}
	for char in str:
		if char not in ret.keys():
			ret.update({char:str.count(char)})
	return (ret)
	
print(char_count('language'))