def fxn():
    pass
if 1==2:
    pass               # use "pass" if u got ntg to do


# actual code
main_pwd=input("Enter the main password: ")
def view():
    pass

def add():
    name=input("Account name : ")
    pwd= input("password: ")
    with open('passwords.txt', 'a') as f:
        



while True:
    mode=input("Want to add a new password or see and existing one? (add/view) or q for quit :")
    if mode=='q':
        break
    elif mode=="view":
        view()
    elif mode=="add":
        add()
    else:
        print("Enter a valid mode")