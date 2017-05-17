<h1>computeAES</h1>
**You found this clue laying around. Can you decrypt it?**
>Encrypted with AES in ECB mode. All values base64 encoded
ciphertext = t1h0qbcOhRQF5E46bsNLimfbcI6egrKP4LHtKR3lT4UdWjhssM8RQSBT7S/8rcRy
key = T5uVzYtuBNv6vwjohslV4w==

<!---->

>Hints:
>
>Try online tools or python

Since we're told that the values are base64 encoded, the first step is to decode them.

Using an online decoder (http://www.motobit.com/util/base64-decoder-encoder.asp) gives us a bunch of garbage:

```
ciphertext = ·Xt©·…äN:nÃKŠgÛpŽž‚²à±í)åO…Z8l°ÏA Sí/ü­Är
key = O›•Í‹nÛú¿è†ÉUã
```

Since the hint told us to try using python as well, chances are the decoded data should be stored as binary to retain information and avoid conflicts with compatibility. Luckily, the same base64 decoding website can export the results as a binary(.bin) file.

Next step is to decrypt the decoded data. We're told the encryption is AES in ECB mode. Again, online tools (http://aes.online-domain-tools.com/) can be used. The cipher text can be uploaded directly. However the key needs to be in plain text or hex. Easiest route here is to convert to hex, since we originally made a binary file to avoid conflicts made by using plain text.

Using Hexfiend, the key becomes:
```
4F9B95CD 8B6E04DB FABF08E8 86C955E3
```
Decrypting the key obtains us the following value:

```
flag{do_not_let_machines_win_1e6b4cf4}
```
