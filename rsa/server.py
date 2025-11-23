import socket

def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

def mi(a,b):
    r1=b; r2=a; t1=0; t2=1
    while r2!=0:
        q=r1//r2
        r=r1%r2
        t=t1-t2*q
        r1,r2 = r2,r
        t1,t2 = t2,t
    if t1<0: t1+=b
    return t1

p=int(input("p: "))
q=int(input("q: "))
e=int(input("e: "))
n=p*q
phi=(p-1)*(q-1)
d=mi(e,phi)

s=socket.socket()
s.bind(("127.0.0.1",5000))
s.listen(1)
conn,_=s.accept()

conn.send(f"{e},{n}".encode())      # send public key
ct=int(conn.recv(1024).decode())     # receive ciphertext
pt = pow(ct,d,n)
print("Decrypted:", pt)

conn.close()
s.close()