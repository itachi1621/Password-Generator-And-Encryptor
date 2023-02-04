from custom_functions.enc_funs import *;
from custom_functions.file_handler import *;


#print (gen_bcrypt(12,'Password1'));
#print (SHAEncrypt('Passweord1',256));


options = ['letters','numbers'];

password = generate_password(24,options);

print (password);