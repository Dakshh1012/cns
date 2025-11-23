import numpy as np

pub=[]
prb=[]
pua=[]
pra=[]

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

def rsa_preprocess(pu,pr):
    global pub,prb,pua,pra
    p=int(input('Enter p'))
    if(is_prime(p)==0):
        print('p is not a prime')
        return

    q=int(input('Enter q'))
    if(is_prime(q)==0):
        print('q is not a prime')
        return
    n=p*q
    phi_n=(p-1)*(q-1)
    e=int(input('Enter e :'))
    if(gcd(e,phi_n)!=1):
        print('rsa not possible with these values as gcd(e,phin ) is not 1')
        exit()
    d=mi(e,phi_n)
    pu.clear()
    pu.extend([e,n])
    print('Public Key : ', pu)
    pr.clear()
    pr.extend([d,n])
    print('Private Key : ', pr)


def rsa_encrypt(pu,m):
    #encryption
    ct=(m**pu[0])%pu[1]
    return ct

def rsa_decrypt(pr,ct):
    #decryption
    pt=(ct**pr[0])%pr[1]
    return pt
    
def main():
    print('Alices keys')
    rsa_preprocess(pua,pra)
    print('Bobs keys')
    rsa_preprocess(pub,prb)
    m=int(input('Enter message: '))
    digisig=rsa_decrypt(pra,m)
    print('Digital Signature of m(Encryption by alices private key): ', digisig)
    ct=rsa_encrypt(pub,digisig)
    print('Cipher text(Encrypted by bobs public key) : ', ct)
    digisig2=rsa_decrypt(prb,ct)
    print('Digital SIgnature as received by receiver: ')
    if digisig==digisig2:
        print('Signature Valid')
    else:
        print('Signature invalid')
        return
    pt=rsa_encrypt(pua,digisig2)
    print('Decrypted cipher text : ', pt)
    
main()