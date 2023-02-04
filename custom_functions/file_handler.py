import os;
import csv;


def exportToCSV(data):
    
    if(not folderExsists('exports')):
        create_folder('exports');

    

    passwordList = [];
    for i in range(len(data)):
        passwordList.append([data[i].password,data[i].encryptionType,data[i].encryptedPassword]);
        
    headers = ['Password', 'Type', 'Encrypted Password'];
    with open('exports/passwords.csv', 'w', newline='',encoding="UTF-8") as file:
        writer = csv.writer(file);
        writer.writerow(headers);
        writer.writerows(passwordList);
    return True;
        
def folderExsists(name):
    if os.path.isdir(name):
        return True;
    else:
        return False;

def file_exsists(file_path):
    if os.path.isfile(file_path):
        return True;
    else:
        return False;

def create_folder(name):

    if (not folderExsists):
        os.makedirs(name);
        return True;
    else:
        return False;

def delete_file(path,name):

    if os.path.isfile(path+name) == True:
        os.remove(path+name);
    return True

