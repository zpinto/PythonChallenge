import pickle

file = open("PythonChallenge5Text.p", "rb")
stuff = pickle.load(file)
file.close()
print(stuff)

for i in range(0, len(stuff)):
    line = ""
    for j in range(0, len(stuff[i])):
        line += stuff[i][j][0] * stuff[i][j][1]
    print(line)

#answer: "http://www.pythonchallenge.com/pc/def/channel.html"
#answer: "http://www.pythonchallenge.com/pc/def/oxygen.html"
