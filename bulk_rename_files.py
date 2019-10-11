import os, shutil, csv, sys, argparse

class file_info:
    hidden_files = ['Thumbs.db', 'ehthumbs.db', '.DS_Store', '.AppleDouble', '.LSOverride']
    file_metadata = ['old_filename', 'new_filename', 'filepath']
    filetypes = ['.png', '.tif', '.jpg', '.doc', '.docx', '.pdf', '.csv']
    filepath = ''
    identifier = 1

    def create_logging_csv(self, renamed_files):
        with open('updated_filenames.csv', 'w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=self.file_metadata)
            writer.writeheader()
            writer.writerows(renamed_files)

    def check_filetype(self, file):
        for filetype in self.filetypes:
            if file.endswith(filetype):
                return filetype

    def prompt_for_choice():
        selection = input('Enter 1 for ')

files = file_info()
files_changed = []

for folder in os.listdir('to_change'):
    for old_filename in os.listdir(folder):
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
