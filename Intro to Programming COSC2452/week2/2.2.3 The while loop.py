import sys
words=['cat', 'window', 'defenestrate']
w=0
while(w<len(words)):
    sys.stdout.write(words[w]+"  "+str(len(words[w])))
    w+=1
