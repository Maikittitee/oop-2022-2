def	update_records(dictionary_record : dict, id : int, property : str, value : any):
	if id not in dictionary_record.keys():
		dictionary_record.update({id:{property:value}})
	else:
		dictionary_record[id].update({property:value})
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


print(update_records(record_collection,1,"tracks",["Rick roll", "Sunshine"]))