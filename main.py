import random
import firebase_admin

s

rom firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("myKeys.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://python-ed-default-rtdb.asia-southeast1.firebasedatabase.app'
})
ref = db.reference('/Crypto')

def encrypt(uinput):
    global gkey
    gkey = ''
    a = """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ !@%^&*()_+1234567890-={}\|;':",<>?`~"""
    key = {}
    fstring = """"""
    list = [random.randint(0, 9), chr(random.randint(65, 90)), chr(random.randint(97, 122)), "@", "%", "&"]
    for i in a:
        def rec_str():
            string = """"""
            for j in range(3):
                string += str(random.choice(list))
            if string not in key.values():
                key[i] = string
            else:
                rec_str()
        rec_str()
    for i in uinput:
        fstring += key[i]
    def c_gkey():
        global gkey
        for i in range(5):
            gkey += str(random.choice(list))
        if gkey not in ref.get():
            ref.update({
                gkey: key
            })
        else:
            c_gkey()
    c_gkey()

    fstring += gkey
    print("WARNING! - Please remember your token, if token is lost then you can't retrieve your data.")
    return fstring

def decrypt(fstring):
    a = """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ !@%^&*()_+1234567890-={}\|;':",<>?`~"""
    tempkey = fstring[-5:]
    if tempkey not in ref.get():
        print("\nYour token id is either expired or Invalid\n")
        en_dec()
    fstring = fstring[:-5]
    data = ref.get()
    for i in data:
        if i == tempkey:
            dkey = data[i]

    finlist = []
    b = 0
    dec_out = """"""
    for i in range(3, len(fstring)+1, 3):
        finlist.append(fstring[b:i])
        b += 3
    for i in finlist:
        try:
            for j in a:

OBOB                    if dkey[j] == i:
OB                        dec_out += j
OB        except:
OB                print("\nYour token id is either expired or Invalid\n")
OB                en_dec()
    dkey = {}
    ref.update({
OB        tempkey: dkey
OB    })
    return dec_out
OB
def en_dec():
    print("Welcome to #404 ED Tool")
OB    print("1): Enter E to Encrypt.")
    print("2): Enter D to Decrypt.")
OB    print("3): Enter Q to Quit.")
    while True:
        choice = input("Enter Your Choice: ")
        if choice == "E" or choice == "e":
            text = input("Enter Your text to encrypt: ")
OB            print(f'Your token is: {encrypt(text)}')
        elif choice == "D" or choice == "d":
            text = input("Enter Your Token to Decrypt: ")
            print(decrypt(text))
        elif choice == "Q" or choice == "q":
            exit()
OB        else:
            print("Invalid Input!")
en_dec()

