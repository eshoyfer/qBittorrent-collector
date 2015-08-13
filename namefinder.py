## Name Finder for Filename ## 

# Returns a string with suggested filename for the .torrent,
# extracted (in a butchered manner) from the encoded bencode.

# Done this way due to apparant issues with decoding bencode of torrent files from BT_backup.
# Quick and dirty: things can go wrong. But the filename is just a suggestion, anyway.

def namefinder(path_to_file):
	rawdata = open(path_to_file).read()
	split_data = rawdata.split(':')[:-1]

	counter = 0
	name_index = 0
	piece_index = 0
	for item in split_data:
		# name_index and piece_index should only be recorded on their first occurance
		if ('name' in item) and (name_index == 0):
			name_index = counter
		if ('piece' in item) and (piece_index == 0):
			piece_index = counter
		counter += 1

	filename = split_data[name_index + 1][:-2] + '.torrent' # Remove the encoding-residue "12" leftover at the end of the name

	return filename

## End Name Finder for Filename ##