import os
import sys
import fileinput
import glob
import shutil

# Windows BT_backup location:
# C:\Users\<user>\AppData\Local\qBittorrent\BT_backup

# In argument:

# (1) Given AppData folder for that user (typically C:\Users\<user>\AppData\Local\qBittorrent\BT_backup)
# as absolute path --> this path used 

# (2) Nothing --> defaults to locating C:\Users\<user>\AppData\Local\qBittorrent\BT_backup

#print sys.argv

## Reading Initial Arguments ## 

if len(sys.argv) > 1:
	# AppData folder supplied
	input_dir = sys.argv[1]
	specified_path = os.path.join(input_dir, 'Local', 'qBittorrent', 'BT_backup')
else:
	# Default 
	# No AppData folder supplied, locate default
	default_path = os.path.join('C:', os.sep, 'Users', os.getenv('username'), 'AppData', 'Local', 'qBittorrent', 'BT_backup')
	specified_path = default_path

if not os.path.exists(specified_path):
	sys.exit("Invalid path!\nThe folder is typically located at C:\Users\<user>\AppData.\nSupply no arguments to attempt finding the default folder.")


## End Reading Initial Arguments ## 

path = 'test.torrent'

## Name Finder for Filename ## 

# Returns a string with suggested filename for the .torrent,
# extracted (in a butchered manner) from the encoded bencode.

# Done this way due to apparant issues with decoding bencode of torrent files from BT_backup.
# Quick and dirty: things can go wrong. But the filename is just a suggestion, anyway.

def namefinder(path_to_file):
	rawdata = open(path).read()
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

	filename = split_data[name_index + 1][:-2] # Remove the encoding-residue "12" leftover at the end of the name

## End Name Finder for Filename ##

## Copy and Rename Files ## 
for this_file in os.listdir(specified_path):
	this_abs_path = os.path.join(specified_path, this_file)
	shutil.copyfile(specified_path, "./")

## End Copy and Rename Files ##

## Misc Testing ## 

#print path
#print rawdata
#print bencode.bdecode(rawdata)


#input_dir = sys.argv[1]
#input_dir_list = os.listdir(input_dir)

#default_path = os.path.join('C:', os.sep, 'Users', os.getenv('username'), 'AppData', 'Local', 'qBittorrent', 'BT_backup')
#specified_path = os.path.join(input_dir, 'AppData', 'Local', 'qBittorrent', 'BT_backup')

#print "default:", default_path
#print "specified_path", specified_path
#print os.listdir(specified_path)
#print sys.argv
#print sys.argv[1]
#print input_dir

## End Misc Testing ##