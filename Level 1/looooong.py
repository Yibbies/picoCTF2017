import sys
import socket
import re

print("Enter the port number to connect to:")
portnumber = input()
if(portnumber<1024 or portnumber>65535):
        exit()

x = socket.socket()
x.connect(("shell2017.picoctf.com", portnumber))

#Regex to extract between quotes
a = re.findall(r"'(.*?)'", x.recv(4096))

#Extracting the letter + number + ending
b = a[0] 			#letter
c = int(a[1])			#letter quantity
d = a[2]			#ending value

#constructing the payload
payload = b * c
payload += d
payload += "\n"

x.send(payload)
sys.stdout.flush()
print(x.recv(4096))

#Source:https://github.com/Idomin/CTF-Writeups/blob/master/PicoCTF-2017/looooong
