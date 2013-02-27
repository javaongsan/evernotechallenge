Alist=[]
N = int(raw_input())
if (N < 1000000):
    for i in range(N):
        choice=int(raw_input())
        if (-2147483648 <= choice <= 2147483647):
            Alist.append(choice)

Alist.sort(reverse=True)
x=1
for s in Alist:
    if x<=4:
        print s
    x=x+1