import hashlib
import os
from cryptography import fernet
from cryptography.fernet import Fernet
import time
import secrets
import string

# functions
    # keys
def writeKey():
    key = Fernet.generate_key()
    with open("db/key.key", "wb") as key_file:
        key_file.write(key)

def loadKey():
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
    print("A unique key has been generated in the 'db' folder. Use it to **manually** decrypt your passwords if you ever forget your master password.")

# def savePass():
#     file = open("db/masterpassword.mpf", "r")
#     hash = file.read
#     print("Enter master password")
#     uimas = input()
#     key = loadKey()
#     fernet = Fernet(key)

#     print('Enter Name of Password:')
#     name = input()
#     print("Enter password")
#     Pass = input()
#     passEncoded = Pass.encode()
#     encrypted = fernet.encrypt(passEncoded)
#     cmd_command = "cd db/ && echo {} > {}.mpf".format(encrypted, name)
#     os.system(cmd_command)

def savePass():
    key = loadKey()
    fernet = Fernet(key)

    print("Enter name of password")
    name = input()
    print("Enter password")
    Pass = input()
    passEncoded = Pass.encode()
    encrypted = fernet.encrypt(passEncoded)
    with open("db/" + name + ".mpf", "wb") as f:
        f.write(encrypted)

def readPass():
    key = loadKey()
    fernet = Fernet(key)
    
    print("Enter name of password to be read")
    rName = "db/" + input() + ".mpf"
    file = open(rName, "r")
    fileCon = file.read().encode("utf-8")
    decrypted = fernet.decrypt(fileCon)
    print(decrypted.decode("utf-8"))


def readpassMAS():
    key = loadKey()
    fernet = Fernet(key)

    print("Enter master password")
    uimas = input()
    with open("db/masterpassword.mpf", "r") as file:
        mpk = file.readline()
        uimasHashed = str(hashlib.sha256(uimas.encode("utf-8")).hexdigest())
    if(mpk.strip() == uimasHashed):
        print("Enter name of password to be read")
        rName = "db/" + input() + ".mpf"
        file = open(rName, "r")
        fileCon = file.read().encode("utf-8")
        decrypted = fernet.decrypt(fileCon)
        print(decrypted.decode("utf-8"))

    else:
        #print("<!ERR!> **invalid master password**")
        raise ValueError("Invalid master password")

def savepassMAS():
    key = loadKey()
    fernet = Fernet(key)

    print("Enter master password")
    uimas = input()
    with open("db/masterpassword.mpf", "r") as file:
        mpk = file.readline()
        uimasHashed = str(hashlib.sha256(uimas.encode("utf-8")).hexdigest())

    if(mpk.strip() == uimasHashed):
        print("Enter name of password")
        name = input()
        print("Enter password")
        Pass = input()
        passEncoded = Pass.encode()
        encrypted = fernet.encrypt(passEncoded)
        with open("db/" + name + ".mpf", "wb") as f:
            f.write(encrypted)

    else:
         raise ValueError("Invalid master password")


def deletepassMAS():
    key = loadKey()
    fernet = Fernet(key)

    print("Enter master password")
    uimas = input()
    with open("db/masterpassword.mpf", "r") as file:
        mpk = file.readline()
        uimasHashed = str(hashlib.sha256(uimas.encode("utf-8")).hexdigest())

    if(mpk.strip() == uimasHashed):
        print("Enter name of password to delete")
        pasName = input()
        if input("Are you sure you want to delete the password of {} (y/n)".format(pasName)) != "y":
            raise ValueError("Operation cancelled by user")
            exit()
        else:
            if(os.path.exists("db/" + pasName + ".mpf")):
                os.remove("db/" + pasName + ".mpf")
                time.sleep(3)
                if(os.path.exists("db" + pasName + ".mpf")):
                    print("Password has been deleted")
                else:
                    raise ValueError("Unknown Error: Password Cannot be Deleted.")

            else:
                raise ValueError("Path does not exist")
    else:
        raise ValueError("Invalid Master Password")

def generatePassword():
    print("Input length of password")
    length = int(input())
    if length <8:
        raise ValueError("Length of password cannot be shorter than 8 characters")
    elif length >=8:
        alphabet = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(alphabet) for i in range(length))
        print(password)
        time.sleep(1)
        if input("Do you want to save this password? (y/n)") != "y":
            exit()
        else:
            key = loadKey()
            fernet = Fernet(key)

            print("Enter master password")
            uimas = input()
            with open("db/masterpassword.mpf", "r") as file:
                mpk = file.readline()
                uimasHashed = str(hashlib.sha256(uimas.encode("utf-8")).hexdigest())

            if(mpk.strip() == uimasHashed):
                print("Enter name of password")
                name = input()
                Pass = password
                passEncoded = Pass.encode()
                encrypted = fernet.encrypt(passEncoded)
                with open("db/" + name + ".mpf", "wb") as f:
                    f.write(encrypted)

            else:
                 raise ValueError("Invalid master password")
    else:
        raise ValueError("Unhandled Exception Error")