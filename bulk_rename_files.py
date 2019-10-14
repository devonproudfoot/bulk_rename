import os, shutil, csv, sys, argparse
from datetime import datetime
import identifiers

class file_info:
    hidden_files = ['Thumbs.db', 'ehthumbs.db', '.DS_Store', '.AppleDouble', '.LSOverride']
    file_metadata = ['old_filename', 'new_filename', 'filepath']
    filetypes = ['.png', '.tif', '.jpg', '.doc', '.docx', '.pdf', '.csv']

    def create_logging_csv(self, renamed_files):
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        csv_name = 'updated_filenames_test_' + date + '.csv'
        with open(csv_name, 'w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=self.file_metadata)
            writer.writeheader()
            writer.writerows(renamed_files)

    def check_filetype(self, file):
        for filetype in self.filetypes:
            if file.endswith(filetype):
                return filetype

    def prompt_for_choice(self):
        selection = input('Enter 1 for ')

files = file_info()
files_changed = []
directory = 'to_change'
current_id = identifiers.next_id

for folder in os.listdir(directory):
    if folder not in files.hidden_files:
        folder_path = os.path.join(directory, folder)
        for old_filename in os.listdir(folder_path):
            if old_filename not in files.hidden_files:
                old_path = os.path.join(folder_path, old_filename)
                file_extension = files.check_filetype(old_filename)
                new_filename = str(current_id) + file_extension
                new_path = os.path.join(folder_path, new_filename)
                shutil.move(old_path, new_path)
                dictionary_changes = {
                    'old_filename' : old_filename,
                    'new_filename' : new_filename,
                    'filepath' : folder
                }
                files_changed.append(dictionary_changes)
                current_id += 1

files.create_logging_csv(files_changed)
