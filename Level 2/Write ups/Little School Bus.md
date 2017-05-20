<h1>Little School Bus</h1>
**Can you help me find the data in this littleschoolbus.bmp?**

>Hints:
>
>- Look at least significant bit encoding!!

We are given an image of a little school bus:

![](../littleschoolbus.bmp)

The hint tells us to consider the least significant bit (LSB) encoding. Chances are we're looking at an example of steganography. 

There's a nice little tool called zsteg(https://github.com/zed-0xff/zsteg) which can detect steganography in png and bmp files.

```bash
zsteg littleschoolbus.bmp
```

zsteg gives us the following results:

```
imagedata           .. text: "~vtsoljmkhigfXVWONOWTV~}"
b1,lsb,bY           .. text: "flag{remember_kids_protect_your_headers_c668}"
b3,r,lsb,xY         .. file: very old 16-bit-int big-endian archive
b4,rgb,msb,xY       .. file: MPEG ADTS, layer I, v2, 112 kbps, 24 kHz, JntStereo
```

We have our flag:

```
remember_kids_protect_your_headers_c668
```

