import urllib.request
#start is "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345"
url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
num = "63579"
res = ""
for i in range (0, 400):
    with urllib.request.urlopen(url + num) as response:
        res = response.read()
        print(res)
        num = ""
    for n in range(0, len(res)):
        if 57 >= res[n] >= 48:
            num += chr(res[n])
    
#answer: "http://www.pythonchallenge.com/pc/def/peak.html"
