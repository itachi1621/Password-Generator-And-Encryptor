from custom_functions.enc_funs import *;
from custom_functions.file_handler import *;
from custom_functions.db_handler import *;


#print (gen_bcrypt(12,'Password1'));
#print (SHAEncrypt('Passweord1',256));


options = ['letters','numbers'];

password =  Password();
passwordList = [];
for i in range(10):

    password.generate_password(24,options)
    password.BcryptEnc(password.password,12)
    passwordList.append(password);
    password = Password();

exportToCSV(passwordList);
   
#passDB = PasswordDB('pdb')

#password.generate_password(24,options)
#password.BcryptEnc(password.password,12)

#passDB.insertPassword(password);

#print (password.encryptedPassword);