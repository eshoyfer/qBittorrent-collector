# qBittorrent-collector

### Info

**qBittorrent** stores the .torrent files of all torrents loaded within the client within a designated folder, paired with .fastresume files with client metadata. In Windows, this directory is located by default at `C:\Users\<user>\AppData\Local\qBittorrent\BT_backup)`.

The .torrent files are not stored with their original filenames (as imported), but with the hashes of the torrent info of the respective .torrent. This tool, **qBittorrent-collector**, iterates over the .torrent files in a source folder, replaces their filename with the original name found in the .torrent metadata, and copies them over to a destination folder. This is intended to help a user migrate or otherwise backup the torrents loaded in qBittorrent.

The original intent was to access the `BT_backup` folder in `AppData` directly, but Windows permissions prevented this. This approach is documented in `old/collector2.py`. The actual tool is `collector.py`, which is dependent on `namefinder.py`.

`namefinder.py` contains the function used for extracting the name from the torrent metadata. Doing it the proper way -- via decoding the bencode and accessing the .torrent metadata dictionary -- led to some issues with torrent files stored in BT_backup, so a butched quick and dirty approach was used instead.

### Usage

**Synopsis**: `python collector.py <source_dir> [<dest_dir>]`

Find your qBittorrent installation's BT_backup folder, located by default on Windows at `C:\Users\<user>\AppData\Local\qBittorrent\BT_backup)`. You likely will not have permission to use this folder directly, so copy/paste the files to a source directory of your choice.

Running `python collector.py <source_dir>` will result in the output files' placement defaulting to `./output` in the directory from which `collector.py` resides. Optionally specify a destination directory as the next parameter.