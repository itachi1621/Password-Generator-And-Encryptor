import os;

def file_exsists(file_path):
    if os.path.isfile(file_path):
        return True
    else:
        return False

def create_folder(path,name):

    if os.path.isdir(path) == False:
        os.mkdir(path)
    if os.path.isdir(path+name) == False:
        os.mkdir(path+name)
    return True

def delete_file(path,name):

    if os.path.isfile(path+name) == True:
        os.remove(path+name)
    return True

