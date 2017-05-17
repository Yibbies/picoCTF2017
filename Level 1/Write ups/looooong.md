<h1>looooong</h1>
**I heard you have some "delusions of grandeur" about your typing speed. How fast can you go at shell2017.picoctf.com:51091?**

>Hints:
>
>- Use the nc command to connect!
>- I hear python is a good means (among many) to generate the needed input.
>- It might help to have multiple windows open

We have an address and port to connect to. We use netcat to connect:

```bash
nc shell2017.picoctf.com 51091
```
Once connected, we are presented with a challenge:

```
To prove your skills, you must pass this test.
Please give me the 'Y' character '776' times, followed by a single '4'.
To make things interesting, you have 30 seconds.
Input:
```
No way we can type this out reliably. Maybe we can get something different by refreshing the connection.

Connecting again gives us:

```
To prove your skills, you must pass this test.
Please give me the 'D' character '564' times, followed by a single '7'.
To make things interesting, you have 30 seconds.
Input:
```
So here we can see that format is the same, but the character to use and quantity changes. Sure, we can try to do this...but effort. Instead, we can use a python program to parse the text and output the answer for us quickly:

```python
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
c = int(a[1])		#letter quantity
d = a[2]			#ending value

#constructing the payload
payload = b * c
payload += d
payload += "\n"

x.send(payload)
sys.stdout.flush()
print(x.recv(4096))

#Source:https://github.com/Idomin/CTF-Writeups/blob/master/PicoCTF-2017/
#           looooong
```

Running the python program gives us our flag:

```
You got it! You're super quick!
Flag: with_some_recognition_and_training_delusions_become_glimpses_cf0c40cbcc7efbd5121222729fff9263
```
