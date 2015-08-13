import os
import sys
import fileinput
import glob

# Windows BT_backup location:
# C:\Users\<user>\AppData\Local\qBittorrent\BT_backup

# In argument:

# (1) Given AppData folder for that user (typically C:\Users\<user>\AppData\Local\qBittorrent\BT_backup)
# as absolute path --> this path used 

# (2) Nothing --> defaults to locating C:\Users\<user>\AppData\Local\qBittorrent\BT_backup

#print sys.argv

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

path = 'test.torrent'
rawdata = open(path).read()
split_data = rawdata.split(':')[:-1]
print rawdata.find('name')
print rawdata.find('piece')

## Name Finder for Filename ## 

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
