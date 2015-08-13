import os
import sys
import fileinput
import glob
import shutil

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