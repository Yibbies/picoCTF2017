##Raw2Hex
**This program just prints a flag in raw form. All we need to do is convert the output to hex and we have it! CLI yourself to /problems/7ed72aec10a93d978ec3542055975d36 and turn that Raw2Hex!**

>Hints:
>
>Google is always very helpful in these circumstances. In this case, you should be looking for an easy solution.

We use our shell to ssh into the server and navigate to the problem directory to see what we have:

```bash
ssh user@shell2017.picoctf.com
cd /problems/7ed72aec10a93d978ec3542055975d36
ls
```

We see two files: flag and raw2hex. With world permissions we cannot do anything with the flag file. We do, however, have executable permissions for raw2hex. Executing it gives us:

```
The flag is:#:3?0R??_?$??SR
```

Given the name of the challenge and the executable, it would be safe to assume that we cannot simply copy and paste the garbage flag text into the answer, so we should convert this to hex. This can be achieved by using the xxd tool. To do this, we pipe the output of the executable into xxd and obtain the hex value of the output:

```bash
# -p: output in postscript plain hexdump style.
./raw2hex | xxd -p
```
We get our flag value in hex:

```
54686520666c61672069733a233a338f3052fec75f009f2485ac5352
```
