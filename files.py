import os
filepath= 'stuff/test.txt'            #ts relative, can use absolute too
if os.path.exists(filepath):
    print(f"The location {filepath} exists")
else:
    print("location doesn't exist twin")
if os.path.isfile(filepath):
    print("Its a file")