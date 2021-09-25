import hashlib
import os
from cryptography.fernet import Fernet

# functions
    # keys
def writeKey():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("db/key.key", "wb") as key_file:
        key_file.write(key)

def loadKey():
    """
    Loads the key from the current directory named `key.key`
    """
    return open("db/key.key", "rb").read()


def setMasPass():
    print('''
    ______  ___   _____ ________  ___  ___   _   _ 
    | ___ \/ _ \ /  ___/  ___|  \/  | / _ \ | \ | |
    | |_/ / /_\ \\ `--.\ `--.| .  . |/ /_\ \|  \| |
    |  __/|  _  | `--. \`--. \ |\/| ||  _  || . ` |
    | |   | | | |/\__/ /\__/ / |  | || | | || |\  |
    \_|   \_| |_/\____/\____/\_|  |_/\_| |_/\_| \_/
                                                
    '''                                               
    )
    print("Set your master password")
    input_master_password = input()
    master_password_hash = hashlib.sha256(input_master_password.encode('utf-8')).hexdigest()
    cmd_command = "cd db/ && echo " + master_password_hash + " > masterpassword.mpf" 
    os.system(cmd_command)
    writeKey()
    print("Master Password has Been Set")
    print("A unique key has been generated in the 'db' folder. Use it to decrypt your passwords if you ever forget your master password.")

def savePass():
    key = loadKey()
    fernet = Fernet(key)

    print('Enter Name of Password:')
    name = input()
    print("Enter password")
    Pass = input()
    passEncoded = Pass.encode()
    encrypted = fernet.encrypt(passEncoded)
    cmd_command = "cd db/ && echo {} > {}.mpf".format(encrypted, name)
    os.system(cmd_command)

def readPass():
    key = loadKey()
    fernet = Fernet(key)
    
    print("Enter name of password to be read")
    rName = "db/" + input() + ".mpf"
    file = open(rName, "r")
    fileCon = file.read().encode()
    decrypted = fernet.decrypt(fileCon)
    
