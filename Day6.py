import sys
n = int(input())
for i in range(n):
    string = input()
    m = len(string)
    for j in range(m):
        if(j%2==0):
            sys.stdout.write(string[j]);
    for k in range(m):
        if(k%2!=0):
            if(k==1):
                sys.stdout.write(" "+string[k]);
            else:
                sys.stdout.write(string[k]);
    print(" ")
    
