import hashlib
import os
from cryptography.fernet import Fernet

# functions
def writeKey():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("db/key.key", "wb") as key_file:
        key_file.write(key)


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
    print('Enter Name of Password:')
    name = input()
    