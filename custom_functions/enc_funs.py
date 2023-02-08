import random;
import string;
import bcrypt;
import hashlib;

class Password:

    def __init__(self):
        self.password = '';
        self.encryptionType = 'None';
        self.encryptedPassword = '';
       



    def generate_password(self,length,options):
        # Generate a random password with n characters
        # Check if options is an array or string
        
        password = "";
        password_opt='';
        for i in range(len(options)):
            if options[i] == 'letters':
                password_opt += string.ascii_letters
            elif options[i] == 'numbers':
                password_opt += string.digits
            elif options[i] == 'special':
                password_opt += string.punctuation
            else:
                return "Error: Invalid option"


        for i in range(length):
            password += random.choice(password_opt)
        self.password = password
        return password

    def encryptBcrypt(self,password,rounds):
        # Generate a bcrypt hash of the password
        # with the number of rounds specified
        # and return it
        self.encryptionType = 'Bcrypt';
        self.password = password;
        self.encryptedPassword = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt(rounds)).decode();
        return self.encryptedPassword

    def BcryptVerify(password,bcrypt_string):
        # Verify a password against a bcrypt hash
        # Return True if the password is correct
        # Return False if the password is incorrect
        return bcrypt.checkpw(password.encode('utf-8'),bcrypt_string.encode('utf-8'));


    #SHA 256, 384, 224, 512, 1
    def SHAEncrypt(self,password,option):
        #Ensure option is only an integer
        if type(option) is not int:
            return "Error: Option must be an Integer"
        #Ensure option is a valid option
        #Conver to int
        option = int(option)
        if option not in [256,384,224,512,1]:
            return "Error: Option must be 256, 384, 224, 512, or 1"
        #Ensure password is a string
        if type(password) is not str:
            return "Error: Password must be a string"
        #Return the hash
        result = '';
        if(option == 256):
            result = hashlib.sha256(password.encode('utf-8'));
        elif(option == 384):
            result = hashlib.sha3_384(password.encode('utf-8'));
        elif(option == 224):
            result = hashlib.sha3_224(password.encode('utf-8'));
        elif(option == 512):
            result = hashlib.sha3_512(password.encode('utf-8'));
        elif(option == 1):
            result = hashlib.sha1(password.encode('utf-8'));
        else:
            return "Error: Option must be 256, 384, 224, 512, or 1";
        self.password = password;
        self.encryptionType = 'SHA'+str(option);
        self.encryptedPassword = result.hexdigest();
        return result.hexdigest();

    def SHAVerify(password,hash,option):
        #Ensure option is only an integer
        if type(option) is not int:
            return "Error: Option must be an Integer"
        #Ensure option is a valid option
        #Conver to int
        option = int(option)
        if option not in [256,384,224,512,1]:
            return "Error: Option must be 256, 384, 224, 512, or 1"
        #Ensure password is a string
        if type(password) is not str:
            return "Error: Password must be a string"
        #Return the hash
        result = '';
        if(option == 256):
            result = hashlib.sha256(password.encode('utf-8'));
        elif(option == 384):
            result = hashlib.sha3_384(password.encode('utf-8'));
        elif(option == 224):
            result = hashlib.sha3_224(password.encode('utf-8'));
        elif(option == 512):
            result = hashlib.sha3_512(password.encode('utf-8'));
        elif(option == 1):
            result = hashlib.sha1(password.encode('utf-8'));
        else:
            return "Error: Option must be 256, 384, 224, 512, or 1";

        if result.hexdigest() == hash:
            return True
        else:
            return False


        