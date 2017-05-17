<h1>Hash101</h1>
**Prove your knowledge of hashes and claim a flag as your prize! Connect to the service at shell2017.picoctf.com:17428
UPDATED 16:12 EST 1 Apr.**

>Hint:
>
>All concepts required to complete this challenge, including simple modular math, are quickly found by googling :)


We are given an address and port number in the question. To connect, we will need to use netcat.

```
nc shell2017.picoctf.com 17428
```

Here we are presented a series randomised challenges:

1. Get the ASCII representation of a binary sequence (http://www.binaryhexconverter.com/).
2. ASCII->hex->decimal (http://www.binaryhexconverter.com/)
3. Modulus math (Just throw numbers at it)
4. MD5 hash decrypt (http://www.md5online.org/)

Completing all the challenges awards us the flag:

```
8b95d8e7ccd0e41b8f989195443a9072
```
