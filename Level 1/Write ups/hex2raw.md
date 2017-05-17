<h1>Hex2Raw</h1>
**This program requires some unprintable characters as input... But how do you print unprintable characters? CLI yourself to /problems/b20c0c219ef2c830da927f80fb7e9cd3 and turn that Hex2Raw!**

>Hints:
>
>Google for easy techniques of getting raw output to command line. In this case, you should be looking for an easy solution.

We use our shell to ssh into the server and navigate to the problem directory to see what we have:

```bash
ssh user@shell2017.picoctf.com
cd /problems/b20c0c219ef2c830da927f80fb7e9cd3
ls
```

There we see 3 files: flag, hex2raw and input. Since we have world permissions, we cannot do anything with the flag and input file, but we can execute the hex2raw file. Doing so gives us this dialogue:

```
Give me this in raw form (0x41 -> 'A'):
88a5e3d5caa34e85e5f36cd55d776568

You gave me:
```

So our task here is to convert a hex value into its raw form and feed it to te executable. We can easily achieve this using pipes and a tool called xxd. Running the following command converts our hex value into a raw value.

```bash
echo 88a5e3d5caa34e85e5f36cd55d776568 | xxd -r -p
```

We get:

```
????ʣN???l?]weh
```

Garbage. Whatever, we can verify if it is correct by piping this into the hex2raw executable since this is what it wanted originally.

```bash
# -r: reverse operation: convert (or patch) hexdump into binary.
# -p: output in postscript plain hexdump style.
echo 88a5e3d5caa34e85e5f36cd55d776568 | xxd -r -p | ./hex2raw
```

We obtain our flag:

```
2bdd0a8259fcada3c12d732c7f3ca98a
```
