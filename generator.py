from custom_functions.menus import *;
import argparse;

#displayPasswordList(passwordList);
#print(passwordList);
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--password", help="Password to encrypt")
#Encrytion method for sha
args = parser.parse_args()
parser.parse_args()



mainMenu();
