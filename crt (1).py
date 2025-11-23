import numpy as np

def euclidean(a,b):
    if(a>b):
        r1=a
        r2=b
    else:
        r1=b
        r2=a
    while (r2!=0):
        q=r1//r2
        r=r1%r2
        r1=r2
        r2=r
    return r1


def mi(a,b):
    if(a<=b):
        r1=b
        r2=a
    else:
        r1=b
        r2=a%b
    if(euclidean(r1,r2)==1): #mi only exists if the numbers are coprime
        t1=0
        t2=1
        while (r2!=0):
            q=r1//r2
            r=r1%r2
            t=t1-t2*q
            r1=r2
            r2=r
            t1=t2
            t2=t
    else:
        print('MI is possible only for coprime numbers')
        exit()
    mi=t1
    if(mi<0):
        mi+=b
    return mi

def crt(c,m,k):
    M=1
    for i in range(0,k):
        M=M*m[i]
    M_val=[]
    for i in range(0,k):
        M_val.append(M//m[i])

    Minv=[]
    for i in range(0,k):
        Minv.append(mi(M_val[i],m[i]))
    cval=0
    print('Residul Results: ')
    for i in range(0,k):
        print(c[i])
        cval+=(c[i]*M_val[i]*Minv[i])%M

    return cval%M


def main():
    n1=int(input('Enter a:'))
    n2=int(input('Enter b:'))
    k=int(input('How many moduli: '))
    m=[]
    for i in range(0,k):
        m.append(int(input('Enter pairwise coprime moduli {i+1}')))
    
    a=[]
    b=[]
    for i in range(0,k):
        a.append(n1%m[i])
        b.append(n2%m[i])

    choice = int(input('1-Addition\n2-Subtraction\n3-Multiplication\n4-Division'))
    c=[]
    if(choice==1):
        for i in range(0,k):
            c.append((a[i]+b[i])%m[i])
    elif(choice==2):
        for i in range(0,k):
            c.append((a[i]-b[i])%m[i])
    elif(choice==3):
        for i in range(0,k):
            c.append((a[i]*b[i])%m[i])
    elif(choice==4):
        for i in range(0,k):
            c.append((a[i]*mi(b[i],m[i]))%m[i])
    else:
        print('Error')
    
    print(crt(c,m,k))


main()


