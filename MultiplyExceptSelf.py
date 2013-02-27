N = int(raw_input("Enter the size of the array: "))
Alist = []

for i in xrange(N):
   Alist.append(raw_input("Enter integer " + str(i+1) + " :"))

for i in xrange(N):
    x=0
    result=1
    for A in Alist:
        if x <> i:
            result=int(result)*int(A)
        x=x+1    
    print result
            