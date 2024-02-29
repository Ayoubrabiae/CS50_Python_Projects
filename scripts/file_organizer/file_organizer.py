from sys import argv, exit
from os import listdir, makedirs
from shutil import move

folder_names = {
    'jpg': 'images',
    'png': 'images',
    'pdf': 'PDFs',
    'txt': 'text',
    'doc': 'documents',
    'xlsx': 'spreadsheets',
    'mp3': 'music',
    'mp4': 'videos',
    'zip': 'archives',
    'html': 'web',
    'py': 'python_code',
    'js': 'javascript_code',
    'css': 'stylesheets',
    'json': 'json_data',
    'xml': 'xml_data',
    'ppt': 'presentations',
    'log': 'logs',
    'exe': 'executables',
    'java': 'java_code',
    'cpp': 'cpp_code',
}

def main():
    folder_path = get_folder_path()
    files_list = get_files(folder_path)
    folders = get_folder_names_by_ext(files_list)
    print(folders)
    create_folders(folders, folder_path)
    move_files(files_list, folder_path)

def get_folder_path():
    if len(argv) > 2:
        exit("Please enter just the path of the folder")
    elif len(argv) < 2:
        exit("Please enter the path of the folder")

    return argv[1]

def get_files(folder_path):
    return listdir(folder_path)

def get_folder_names_by_ext(files_list):
    folders = set()
    for file in files_list:
        extension = file.split(".")[len(file.split("."))-1]
        folders.add(extension)
    return folders

def create_folders(folders, path):
    for folder in folders:
        try:
            makedirs(f"{path}/{folder}")
        except FileExistsError:
            print("The file aleardy exist")
            pass

def move_files(files, path):
    for file in files:
        extension = file.split(".")[len(file.split("."))-1]
        move(f"{path}/{file}", f"{path}/{extension}")

main()