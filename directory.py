import requests
import sys

dir_list = open("wordlist.txt").read()
dir_splitted = dir_list.splitlines()

for dirs in dir_splitted:
    dir_enum = f"http://{sys.argv[1]}/{dirs}.html"
    req = requests.get(dir_enum)
    
    if req.status_code == 404:
        pass
    else:
        print("Founded: ",dir_enum)