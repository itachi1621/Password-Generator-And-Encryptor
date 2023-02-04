import sqlite3;

class PasswordDB:
    def __init__(self,db_name):
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor();
        cursor.execute("CREATE TABLE IF NOT EXISTS PASSWORDS (PASSWORD TEXT,TYPE TEXT,ENCPASSWORD TEXT)");
        connection.commit();
        connection.close()
        self.dbname = db_name+'.db'


    
    def insertPassword(self,Password):
        connection = sqlite3.connect(self.dbname);
        cursor = connection.cursor();
        cursor.execute("INSERT INTO PASSWORDS (PASSWORD,TYPE,ENCPASSWORD) VALUES (?,?,?)",(Password.password,Password.encryptionType,Password.encryptedPassword));
        connection.commit();
        connection.close();

    def getPasswords(self):
        connection = sqlite3.connect(self.dbname);
        cursor = connection.cursor();
        cursor.execute("SELECT * FROM PASSWORDS");
        passwords = cursor.fetchall();
        connection.close();
        return passwords;

    def resetDB(self):
        connection = sqlite3.connect(self.dbname);
        cursor = connection.cursor();
        cursor.execute("DROP TABLE IF EXISTS PASSWORDS");
        cursor.execute("CREATE TABLE PASSWORDS (PASSWORD TEXT,TYPE TEXT,ENCPASSWORD TEXT)");
        connection.commit();
        connection.close();



