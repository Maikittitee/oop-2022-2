def	add_score(subject_score:dict, student:str ,subject:str, score:int):
	if (student not in subject_score.keys()):
		subject_score.update({student:{subject : score}})
	else:
		subject_score[student].update({subject : score})
	return (subject_score)

def calc_average_score(subject_score:dict):

	ret_dict={}

	for ele in subject_score.keys():
		ret_dict.update({ele : "{:.2f}".format(sum(subject_score[ele].values())/len(subject_score[ele].values()))})

	return (ret_dict)

my_dict = {}

add_score(my_dict,"65010030","math",9)
add_score(my_dict,"65010034","math",100)
add_score(my_dict,"65010030","eng",10)
add_score(my_dict,"65010034","eng",7)
print(my_dict)

print(calc_average_score(my_dict))
