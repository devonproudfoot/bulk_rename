import os, shutil, csv, hashlib, sys, argparse

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', help='Enter the path to the files to be renamed')
    parser.add_argument('filetype', help='Enter the filetype, currently only allows for tif or jpg')
    args = parser.parse_args()
    filepath = args.filepath.strip()
    filetype = args.filetype.strip()
    return filepath, filetype

def get_checksum(path):
    hash_md5 = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def logging_csv(header, data_entries, csv_file):
    with open(csv_file, 'w') as spreadsheet:
        writer = csv.DictWriter(spreadsheet, fieldnames=header)
        writer.writeheader()
        writer.writerows(data_entries)

directory, file_question = get_args()

if 'tif' in file_question:
    file_type = '.tif'
elif 'jpg' in file_question:
    file_type = '.jpg'
else:
    print('\nPlease enter a valid filetype!')
    sys.exit()

header = ['old_filename', 'old_checksum', 'old_file_size', 'new_filename', 'new_checksum', 'new_file_size', 'valid?']
rows = []

two_millions = 20070000

for old_filename in os.listdir(directory):
    if old_filename.endswith(file_type):
        old_path = os.path.join(directory, old_filename)
        old_checksum = get_checksum(old_path)
        old_file_size = os.path.getsize(old_path)
        new_filename = str(two_millions) + file_type
        new_path = os.path.join(directory, new_filename)
        shutil.move(old_path, new_path)
        new_checksum = get_checksum(new_path)
        new_file_size = os.path.getsize(new_path)
        if old_checksum == new_checksum and old_file_size == new_file_size:
            valid = 'VALID'
        else:
            valid = 'ERROR'
        dictionary = {'old_filename' : old_filename, 'old_checksum' : old_checksum, 'old_file_size' :old_file_size, 'new_filename' : new_filename, 'new_checksum' : new_checksum, 'new_file_size' : new_file_size, 'valid?' : valid}
        rows.append(dictionary)
        two_millions += 1
        print('Renamed ' + old_filename + ' to ' + new_filename)

csvfile = 'first_set_renamed_files.csv'

logging_csv(header, rows, csvfile)

print('\nRenaming complete! Open ' + csvfile + ' to review the results and ensure the integrity of the files!')
