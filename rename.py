import os
import sys
import hashlib
from send2trash import send2trash

#from stack overflow
def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


import easygui

path = easygui.diropenbox()

#if len(sys.argv) != 2:
#    print("Please enter path to rename:")
#    exit()

for (dirpath, dirnames, filenames) in os.walk(path):
    #print(dirpath, dirnames, filenames)
    for name in filenames:
        if name[0] == "." or '.' not in name:
            continue
        path = os.path.join(dirpath,name)
        ext = name.split(".")[-1]
        if ext == "jfif" or ext == "jpeg":
            ext = "jpg"
        if ext not in {"jpg","jpeg","png"}:
            continue
            
        #generate md5 name
        newname = md5(path) + "." + ext
        newpath =  os.path.join(dirpath,newname)
        if newpath != path:            
            if not os.path.exists(newpath):
                #pass
                os.rename(path,newpath)
                print(name,"->",newname)
            else:
                print("File exists:",newname)
                #os.remove(path)
                send2trash(path)
print("Done")