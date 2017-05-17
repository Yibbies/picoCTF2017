<h1>WorldChat</h1>
**We think someone is trying to transmit a flag over WorldChat. Unfortunately, there are so many other people talking that we can't really keep track of what is going on! Go see if you can find the messenger at shell2017.picoctf.com:38798. Remember to use Ctrl-C to cut the connection if it overwhelms you!**

>Hints:
>
>There are cool command line tools that can filter out lines with specific keywords in them. Check out 'grep'! You can use the '|' character to put all the output into another process or command (like the grep process)

We're given an address and a port. Easiest way to connect is to use the netcat tool. Connect using the following command:

```bash
nc shell2017.picoctf.com 38798
```

Connecting give us some scrolling introduction dialogue:

```
worldchat v2.3002.4
setting up readonly client..done
connecting to feed....done
Welcome to WORLDCHAT!
```

Then we get overwhelmed with messages. Lets grep for flag and see what we get:

```bash
nc shell2017.picoctf.com 38798 | grep flag
```

After some delay, we get a bunch of messages from multiple individuals with flag in their name (ihazflag, personwithflag, flagperson and whatisflag). Not good enough, we still need to refine this down further. Reading the messages posted by the flag people we can see that the person we are interested in is flagperson. Lets alter our grep filter:

```bash
nc shell2017.picoctf.com 38798 | grep flagperson
```
Again after some delay, we get:

```
06:54:20 flagperson: this is part 1/8 of the flag - 3572
06:54:26 flagperson: this is part 2/8 of the flag - dd03
06:54:27 flagperson: this is part 3/8 of the flag - 4e91
06:54:29 flagperson: this is part 4/8 of the flag - 5f49
06:54:30 flagperson: this is part 5/8 of the flag - 3120
06:54:30 flagperson: this is part 6/8 of the flag - 885d
06:54:33 flagperson: this is part 7/8 of the flag - 41d5
06:54:35 flagperson: this is part 8/8 of the flag - 46c7
```
Combining the pieces we get our flag:

```
3572dd034e915f493120885d41d546c7
```
