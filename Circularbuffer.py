import datetime

def keepArraySize():
    if len(Alist) > N:
        z=len(Alist)-N
        RemoveFromArray(z)

def RemoveFromArray(z):
    if z <= len(Alist):
        Alist.sort(key=lambda tup: tup[0]) 
        for y in xrange(z):
            Alist.pop(0)

N = int(raw_input())

if (0 <= N <= 10000):
    Alist=[]
    for i in xrange(50000):
        choice=raw_input()
        if len(choice)<= 20000000:
            if choice.startswith("A "):
                for x in xrange(int(choice.split(" ")[1])):
                    Alist.append((datetime, raw_input()))
            elif choice.startswith("R "):
                z = int(choice.split(" ")[1])
                RemoveFromArray(z)
            elif choice=="L":
                for s in Alist:
                    print s[1]
            elif choice=="Q":
                break
            keepArraySize()
