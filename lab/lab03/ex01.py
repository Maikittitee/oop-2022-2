def	add_score(subject_score:dict, subject:str, score:int):
	subject_score.update({subject:score})
	return (subject_score)

def calc_average_score(subject_score:dict):
	return ("{:.2f}".format(sum(subject_score.values())/len(subject_score)))

my_dict = {}
add_score(my_dict,"math",9)
add_score(my_dict,"sci",8)
print(calc_average_score(my_dict))

