import sys;
sys.path.append('../');
from custom_functions.enc_funs import *;
from custom_functions.file_handler import *;
from custom_functions.db_handler import *;

def mainMenu():
    try:
        print('''Following options are available

            1.)Generate a password
            2.)Encrypt a password using(SHA,BCRYPT)
            3.)Verify a password using(SHA,BCRYPT)
            4.)Export all database entires to CSV
            5.)Exit
        ''')
        ui=input('Please enter your selection [1-5]: ')
        #Check if input is a number
        if (not ui.isdigit()):
            raise ValueError
        #Convert to int
        ui = int(ui)
        if (ui == 1):
            passwordGenerationMenu();
        elif (ui == 2):
            pass;
    except ValueError:
        print('Please enter a valid option')
        mainMenu();
        
def passwordGenerationMenu(pass_gens=0, pass_len=0, pass_opt=[],passwordList=[],state='start'):

    max_pass_gen = 9999;
    min_pass_len = 8;
    max_pass_len = 256;
    valid_options = ['letters','numbers','special'];
    if(state == 'start'):
        try:
            if(pass_gens == 0) :
                pass_gens=input('Input number of passwords to be generated leave blank for 1: ');
            #check if input is blank
            if pass_gens == '':
                pass_gens = '1';
                
            #Check if input is a number
            if not pass_gens.isdigit():
                pass_gens = 0
                raise ValueError
            #Check if input is within range
            if int(pass_gens) > max_pass_gen or int(pass_gens) < 1:
                pass_gens = 0
                raise ValueError
            if(int(pass_len) == 0):
                pass_len=input('Input length per password leave blank for default minimum of 8 : ')
                #Check if input is blank
                if pass_len == '':
                    pass_len = str(min_pass_len)
                #Check if input is a number
                if not pass_len.isdigit():
                    pass_len = 0
                    raise ValueError
                #Check if input is within range
                if int(pass_len) > max_pass_len or int(pass_len) < min_pass_len:
                    pass_len = 0
                    raise ValueError
            print('''Password Options
            1.)Letters
            2.)Numbers
            3.)Special Characters''')
            pass_opt=input('Input password options seperated by commas e.g 1,2/1,3 etc leave blank for default of option 1.: ')
            #Check if input is blank
            if pass_opt == '':
                pass_opt = '1'
            #Delimit input by ,
            pass_opt = pass_opt.split(',')
            #Check list for valid numbers
            for i in range(len(pass_opt)):
                if not pass_opt[i].isdigit():
                    pass_opt = []
                    raise ValueError
                if int(pass_opt[i]) > 3 or int(pass_opt[i]) < 1:
                    pass_opt = []
                    raise ValueError
                # Map pass_opt to valid password options
                pass_opt[i] = valid_options[int(pass_opt[i])-1]
            #print (pass_opt)
        
            password = Password();#Create new Password Object
            passwordList = [];#List for storing generated objects
            for i in range(int(pass_gens)):
                password.generate_password(int(pass_len),pass_opt);
                passwordList.append(password);
                password = Password();
            #Print passwoerd list
            for i in range(len(passwordList)):
                print('Password #', i+1 , ': ',passwordList[i].password);
            
            

        except ValueError:
            input("Invalid input, please hit enter to continue")
            #Reload with valid data
            
            passwordGenerationMenu(pass_gens,pass_len,pass_opt,passwordList);
        #Begin creating passwords
        #pass_gens = int(pass_gens);#Cast to appropriate format
        #pass_len = int(pass_len);    
        
    
    try:
        print('''Following options available

        1.)Encrypt generated passwords (SHA,Bcrypt)
        2.)Export generated passwords to CSV
        3.)Save to Database
        4.)Return to main menu
        5.)Exit    
        ''')

        ui = input('Please enter your selection [1-5]: ')
        
        if (not ui.isdigit()):
            raise ValueError
        ui = int(ui)

        if(ui < 1 or ui > 5):
            raise ValueError
        
        if (ui == 1):
            passwordEncryptionMenu(passwordList);
        elif (ui == 2):
            exportToCSV(passwordList);
            print('Records saved')
            mainMenu();
        elif (ui == 3):
            passDB = PasswordDB('pdb')
            for i in range(len(passwordList)):
                passDB.insertPassword(passwordList[i]);#Not the most efficient way, might replace later
            print('Records saved')
            mainMenu();
        elif (ui == 4):
            mainMenu();
        elif (ui == 5):
            exit();
        
    
        #Convert to int
    except ValueError:
        input('Please enter a valid option, press enter to continue.');
        passwordGenerationMenu(pass_gens,pass_len,pass_opt,passwordList,state='end');
    
    
    
    

def passwordEncryptionMenu(passwords = [],rounds=0,state='start'):
    if(state == 'start'):
        min_rounds=8;
        max_rounds=19;

        try:
            if(len(passwords) == 0):
                print('''Following options available
                1)Encrypt a password using bcrypt.
                2)Encrypt a password using SHA.
                3)Return to main menu
                4)Exit
                ''')
                ui = input('Please enter your selection [1-4]: ')
                if (not ui.isdigit()):
                    raise ValueError
                ui = int(ui)
                if(ui < 1 or ui > 4):
                    raise ValueError
                if (ui == 1):
                    password = input('Please enter password to be encrypted: ');
                    if(password == "" or password == " " or len(password) < 8):
                        raise ValueError

                    rounds = input('Please enter number of rounds to be used [8-19] leave blank to use default of 10: ');
                    if(rounds == ""):
                        rounds = "10";
                    if (not rounds.isdigit()):
                        raise ValueError
                    rounds = int(rounds)
                    if(rounds < min_rounds or rounds > max_rounds):
                        raise ValueError
                    password = Password();
                    password.password = password.encryptBcrypt(password,rounds);
                    print('Encrypted password: ',password.password);
                    passwordEncryptionMenu(passwords);



                
            else:
                print('''Following options available
                1)Encrypt generated passwords using bcrypt.
                2)Encrypt generated passwords using SHA.
                3)Return to main menu
                4)Exit
                ''')
                ui = input('Please enter your selection [1-4]: ')
                if (not ui.isdigit()):
                    raise ValueError
                ui = int(ui)
                if(ui < 1 or ui > 4):
                    raise ValueError
                if (ui == 1):
                    rounds = input('Please enter number of rounds to be used [8-19] leave blank to use default of 10: ');
                    if(rounds == ""):
                        rounds = "10";
                    if (not rounds.isdigit()):
                        raise ValueError
                    rounds = int(rounds)
                    if(rounds < min_rounds or rounds > max_rounds):
                        raise ValueError
                    for i in range(len(passwords)):
                        passwords[i].password = passwords[i].encryptBcrypt(passwords[i].password,rounds);
                        print ('Password ', i+1,' of ',len(passwords),' encrypted: '+passwords[i].encryptedPassword);
                    print('Passwords encrypted');
                    passwordEncryptionMenu(passwords);
            
            



        except ValueError:
            input('Invalid input, please hit enter to continue');
            passwordEncryptionMenu(passwords);
    try:
        print('''Following options available

        1.)Export generated passwords to CSV
        2.)Save to Database
        3.)Return to main menu
        4.)Exit    
        ''')

        ui = input('Please enter your selection [1-5]: ')
        
        if (not ui.isdigit()):
            raise ValueError
        ui = int(ui)

        if(ui < 1 or ui > 5):
            raise ValueError
        
        
        if (ui == 1):
            exportToCSV(passwords);
            print('Records saved')
            mainMenu();
        elif (ui == 3):
            passDB = PasswordDB('pdb')
            for i in range(len(passwords)):
                passDB.insertPassword(passwords[i]);#Not the most efficient way, might replace later
            print('Records saved')
            mainMenu();
        elif (ui == 4):
            mainMenu();
        elif (ui == 5):
            exit();
        
    
        #Convert to int
    except ValueError:
        input('Please enter a valid option, press enter to continue.');
        passwordEncryptionMenu(passwords,state='end');
    
