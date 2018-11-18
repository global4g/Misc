#!/usr/bin/python
def getScore(word):
    return sum(ord(i)-65 + 1 for i in word)


#/usr/share/wordlists/rockyou.txt
#/usr/share/dict/american-english

with open("/usr/share/dict/american-english") as f:
    content = f.readlines()
content = [x.strip().upper() for x in content] 

scores = map(getScore, content)

for p in filter(lambda x:x[1]==100, zip(content,scores)):
    print p
