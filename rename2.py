import os, shutil, csv, sys, argparse

class file_info:
    hidden_files = ['Thumbs.db', 'ehthumbs.db', '.DS_Store', '.AppleDouble', '.LSOverride']
    file_metadata = ['old_filename', 'new_filename', 'filepath']
    filetypes = ['.png', '.tif', '.jpg', '.doc', '.docx', '.pdf', '.csv']
    filepath = ''
    identifier = 1
    logging_csv = 'updated_filenames.csv'

    def get_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('filepath', help='Drag the path to the folder.  Is not recursive!')
        parser.add_argument('identifier', type=int, help='Enter the identifier that you would like to start with.  Only works with numbers.')
        args = parser.parse_args()
        self.filepath = args.filepath
        self.identifier = args.identifier

    def create_logging_csv(self, renamed_files):
        with open(self.logging_csv, 'w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=self.file_metadata)
            writer.writeheader()
            writer.writerows(renamed_files)

    def check_filetype(self, file):
        for filetype in self.filetypes:
            if file.endswith(filetype):
                return filetype

files = file_info()
files.get_args()
directory = os.path.join('to_change', files.filepath)
files_changed = []

for old_filename in os.listdir(directory):
    if old_filename not in files.hidden_files:
        old_path = os.path.join(directory, old_filename)
        file_extension = files.check_filetype(old_filename)
        new_filename = str(files.identifier) + file_extension
        new_path = os.path.join(directory, new_filename)
        shutil.move(old_path, new_path)
        dictionary_changes = {
            'old_filename' : old_filename,
            'new_filename' : new_filename,
            'filepath' : directory
        }
        files_changed.append(dictionary_changes)
        files.identifier += 1

files.create_logging_csv(files_changed)
