string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
new = ""
for i in range(0, len(string)):
    if ord(string[i]) >= 97 and ord(string[i]) <= 122:
        if(ord(string[i])+2) == 123:
            temp = chr(97)
        elif(ord(string[i])+2) == 124:
            temp = chr(98)
        else:
            temp = chr((ord(string[i])+2))
        new += temp
    else:
        new += string[i]

print(new)

#translate "map"

string2 = "map"
new2 = ""
for i in range(0, len(string2)):
    if ord(string2[i]) >= 97 and ord(string2[i]) <= 122:
        if(ord(string2[i])+2) == 123:
            temp = chr(97)
        elif(ord(string2[i])+2) == 124:
            temp = chr(98)
        else:
            temp = chr((ord(string2[i])+2))
        new2 += temp
    else:
        new2 += string[i]

print(new2)

#http://www.pythonchallenge.com/pc/def/ocr.html
