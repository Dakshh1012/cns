import socket

s=socket.socket()
s.connect(("127.0.0.1",5000))

e,n = map(int, s.recv(1024).decode().split(","))   # receive public key
m=int(input("Message: "))
ct = pow(m,e,n)
s.send(str(ct).encode())
print("Cipher sent:", ct)

s.close()