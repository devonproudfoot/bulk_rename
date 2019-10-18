import os, shutil, csv, sys, argparse
from datetime import datetime
import identifiers

class file_info:
    hidden_files = ['Thumbs.db', 'ehthumbs.db', '.DS_Store', '.AppleDouble', '.LSOverride']
    file_metadata = ['old_filename', 'new_filename', 'filepath']
    filetypes = ['.png', '.tif', '.jpg', '.doc', '.docx', '.pdf', '.csv']

    def create_logging_csv(self, renamed_files):
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        csv_name = 'updated_filenames_' + date + '.csv'
        with open(csv_name, 'w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=self.file_metadata)
            writer.writeheader()
            writer.writerows(renamed_files)

    def check_filetype(self, file):
        for filetype in self.filetypes:
            if file.endswith(filetype):
                return filetype

    def logging_csv_to_dictionary(self, spreadsheet_file):
        new_dictionary = []
        with open(spreadsheet_file) as spreadsheet:
            return True

    def prompt_for_choice(self):
        selection = input('Enter 1 if you are renaming new files, or 2 if you are renaming from a spreadsheet: ')
        if selection == '1':
            return 1
        elif selection == '2':
            return 2
        else:
            print('Invalid response! Run script again and choose 1 or 2!')
            sys.exit()

files = file_info()
files_changed = []
directory = 'to_change'
current_id = identifiers.next_id
choice = files.prompt_for_choice()

if choice == 1:
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
elif choice == 2:
    files_to_change_path = 'change_from_csv'
    csv_for_renaming = 'for_renaming.csv'
    with open(csv_for_renaming) as csv:
        csv_reader = csv.DictReader(csv)
        for row in csv_reader:
            new_filename = row['new_filename'].replace('.tif', '.jpg')
            old_filename = row['old_filename'].replace('.tif', '.jpg')
            full_old_filepath = os.path.join(files_to_change_path, row['path'], old_filename)
            full_new_filepath = os.path.join(files_to_change_path, row['path'], new_filename)
            if os.path.exists(full_old_filepath):
                shutil.move(full_old_filepath, full_new_filepath)
                dictionary_changes = {
                    'old_filename' : old_filename,
                    'new_filename' : new_filename,
                    'filepath' : row['path']
                }
                files_changed.append(dictionary_changes)
            else:
                dictionary_changes = {
                    'old_filename' : old_filename,
                    'new_filename' : 'ALERT: File does not exist',
                    'filepath' : row['path']
                }
                files_changed.append(dictionary_changes)

    files.create_logging_csv(files_changed)