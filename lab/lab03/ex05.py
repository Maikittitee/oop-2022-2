def	update_records(dictionary_record : dict, id : int, property : str, value : str):
	if value == "": #Try to delete Property
		if (id not in dictionary_record.keys()): # make sure that have id of the property
			return (f"ID:{id} not found")
		elif (property not in dictionary_record[id].keys()): # make sure that have the property
			return (f"Property:{property} not found")
		else: # pop (delete) the property
			dictionary_record[id].pop(property)
		return (dictionary_record)
	if id not in dictionary_record.keys(): #if the id is not exist, then create new id
		dictionary_record.update({id:{property:value}})
	if property == "tracks": 
		if "tracks" not in dictionary_record[id].keys(): # if that id not contain tracks key, then it will create new list that contain values in there
			dictionary_record.update({id:{"tracks":[value]}})
		else: #if tracks was contained , then will append input value to the list
			dictionary_record[id]["tracks"].append(value)
	else:
		dictionary_record[id].update({property:value}) #nomal case update property and value
	return (dictionary_record)



record_collection = {
  2548: {
    "albumTitle": 'Slippery When Wet',
    "artist": 'Bon Jovi',
    "tracks": ['Let It Rock', 'You Give Love a Bad Name']
}, 2468: {
    "albumTitle": '1999',
    "artist": 'Prince',
    "tracks": ['1999', 'Little Red Corvette']
}, 1245: {
    "artist": 'Robert Palmer',
	"tracks": [] },
  5439: {
    "albumTitle": 'ABBA Gold'
}}


print(update_records(record_collection,5439,"albumTitle",""))