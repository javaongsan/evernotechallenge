Alist = dict()
Alist[None] = -1


N = int(raw_input())
if (0 < N < 300000 ):
    for i in range(N):
        choice=raw_input()
        if (0 < len(choice) < 25):
            try:
                Alist[choice] += 1
            except:
                Alist[choice] = 1   

N = int(raw_input())
if N <= len(Alist):
    l = Alist.items()
    l.sort()
    l.sort(key=lambda tup: tup[1], reverse=True)
    x=1
    for s in l:
        if x<=N :
            print s[0]
        else:
            break
        x=x+1