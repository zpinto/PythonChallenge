#start "http://www.pythonchallenge.com/pc/def/zip.html"

#put this source in a folder with channel.zip and the unzipped contents of the channel.zip

import zipfile
from zipfile import ZipFile

ext = ".txt"
num = "90052"
inf = []
res = ""
string = ""

with ZipFile("channel.zip", "r") as myzip:
        inf = myzip.infolist()

for i in range (0, 910):
    for item in inf:
        if (num + ext) == item.filename:
            if str(item.comment)[2] == "\\":
                print(string)
                string = ""
            else:
                string += str(item.comment)[2]
            
    file = open((num + ext), "rb")
    res = file.read()
    num = ""
   
    for n in range(0, len(res)):
        if 57 >= res[n] >= 48:
            num += chr(res[n])
    
print(string)

#answers: "http://www.pythonchallenge.com/pc/def/hockey.html"
