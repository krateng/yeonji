Install with `pip install yeonji`

# borgsize

Lists sizes of all backups in a borg repository. Type `borgsize *repopath*`, e.g. `borgsize ~/myrepos/coolrepo`.

# fsclean

Clean unicode filenames in a directory tree. Use `--dryrun` to check what would be renamed. Existing files will not be overwritten.

# me2dlc

Installs ME2 DLCs from exe files on Linux using Steam Proton. Navigate to directory with files, then run `me2dlc`. Requires protontricks.

# ytdlj

Merges any number of local files / youtube videos into a new file. Type `ytdlj *URLs/files* *outputname*`, e.g. `ytdlj party1.mkv ../party2.mkv https://www.youtube.com/watch?v=b3_lVSrPB6w fullvideo.mkv`.

# yttag

Download a video's audio and immediately id3-tag it according to command line arguments or supplied files. The script will look for `artist`,`albumartist`,`album` and `title` in `metadata.yml` files in this directory and up to three parent directories, but the command line flags will always have preference.
