import numpy as np
#sender alice
#receiver bob
def is_prime(a):
    for i in range(2,a):
        if(a%i)==0:
            return 0
    return 1

def gcd(a,b):
    if(a>b):
        r1=a
        r2=b
    else:
        r1=b
        r2=a
    while r2!=0:
        q=r1//r2
        r=r1%r2
        r1=r2
        r2=r
    return r1

def mi(a,b):
    r1=b    
    r2=a
    t1=0
    t2=1
    while r2!=0:
        q=r1//r2
        r=r1%r2
        t=t1-t2*q
        r1=r2
        r2=r
        t1=t2
        t2=t
    mi=t1
    if(mi<0):
        mi+=b
    return mi


def rsa(p,q,m):
    n=p*q
    phi_n=(p-1)*(q-1)
    e=int(input('Enter e :'))
    if(gcd(e,phi_n)!=1):
        print('rsa not possible with these values as gcd(e,phin ) is not 1')
        exit()
    d=mi(e,phi_n)
    pu=[e,n]
    print('Public Key : ', pu)
    pr=[d,n]
    print('Private Key : ', pr)
    #encryption
    ct=(m**pu[0])%n
    print('Cipher Text: ', ct)
    #decryption
    pt=(ct**pr[0])%n
    print("Decrypted Cipher Text", pt)

def main():
    p=int(input('Enter p'))
    if(is_prime(p)==0):
        print('p is not a prime')
        return

    q=int(input('Enter q'))
    if(is_prime(q)==0):
        print('q is not a prime')
        return
    
    m=int(input('Enter message'))
    m=m%(p*q)
    rsa(p,q,m)

main()