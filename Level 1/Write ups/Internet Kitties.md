##Internet Kitties
**I was told there was something at IP shell2017.picoctf.com with port 42354. How do I get there? Do I need a ship for the port?**

>Hints:
>
>- Look at using the netcat (nc) command!
>- To figure out how to use it, you can run "man nc" or "nc -h" on the shell, or search for it on the interwebz

This one is pretty easy, just connect to the address and specify the port. The easiest way to do this is using the tool netcat:

```bash
nc shell2017.picoctf.com 42354
```

Connecting using this information returns the flag:

```
Yay! You made it!
Take a flag!
74d4fd0abc13a085d6d60489db227dfd
```

