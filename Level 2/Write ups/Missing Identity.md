<h1>Missing Identity</h1>
<b>Turns out, some of the files back from Master Challenge 1 were corrupted. Restore this one file and find the flag. Update 16:26 EST 1 Apr If you feel that you are close, make a private piazza post with what you have, and an admin will help out. The flag starts with the character z.</b>

>Hints:
>
>- What file is this?
>- What do you expect to find in the file structure?
>All characters in the file are lower case or numberical. There will not be any zeros.

The third hint tells us the file is in hex, but before that lets runs strings on the file, while grepping for a flag:

```bash
strings file | grep flag
```

We are given:

```
flag.png
nottheflag1.png
nottheflag2.png
nottheflag3.png
nottheflag4.png
nottheflag5.png
nottheflag6.png
nottheflag7.png
flag.pngPK
nottheflag1.pngPK
nottheflag2.pngPK
nottheflag3.pngPK
nottheflag4.pngPK
nottheflag5.pngPK
nottheflag6.pngPK
nottheflag7.pngPK
```

So we can see there a bunch of red herrings here as well. Lets open the file in Hexfiend.

We can see at the beginning there is a XXXXXX. Seems like we need to repair this file. So to do that we need to know what type of file it is. The strings query from before gave us png and pngPK. This tells us the file is a compressed archive (PKZip) of png images. 

A Google search tells us the header of a PKZip file should contain:

```
\x50\x4b\x03\x04
```

Lets put these values in and append the left over space with 0's. Now lets look at the archive contents: 

```bash
unzip file
```

We get our flag.png image:

![](../../resources/78537ff403ff488f5f8edc21bc513856.png)

Lets submit our flag as the image text.