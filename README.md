# Bulk Renaming Scripts

This repository currently contains scripts for renaming entire folders of access copies of photographs to a unique identifier, and then renaming the preservation copy with that same unique identifier.  These can also rename preservation copies first, followed by the access copy if need be.  These scripts currently run with python3 and require the installation of [hashlib](https://docs.python.org/3.7/library/hashlib.html).

_It is recommended that you test the scripts on copies of the files._

### Step 1
##### [bulk_rename.py](https://github.com/devonproudfoot/bulk_rename/blob/master/bulk_rename.py)

The first script requires two arguments, the path to the folder with the files to be renamed, as well as the type of files.

Ex.
'''
python3 bulk_rename.py 'Desktop/projects/folder_with_jpgs' jpg
'''

After running the script, a spreadsheet will be created in the folder that the script is located.  The spreadsheet will have the original filenames, as well as the new filenames.  It also includes the checksums and file sizes to ensure that the renamed file has not been altered beyond the filename (hopefully this is implemented correctly!) If 'ERROR' is found anywhere in the 'valid?' column, an issue has occurred. Do not delete this file, it is needed for the second script!

### Step 2
##### [rename_from_spreadsheet.py](https://github.com/devonproudfoot/bulk_rename/blob/master/rename_from_spreadsheet.py)

The second script also requires two arguments, the path to the folder with the files to be renamed, as well as the type of files.

Ex.
'''
python3 rename_from_spreadsheet.py 'Desktop/projects/folder_with_tifs' tif
'''

This script will utilize the spreadsheet from first script, and will only files that were renamed initially with their new identifier.  A second spreadsheet will be created with the old/new filenames, as well as checksums and file sizes.  As with the original spreadsheet, if 'ERROR' is found anywhere in the 'valid?' column, an issue has occurred.

PLEASE HAVE FUN IT'S A WORK IN PROGRESS : )
