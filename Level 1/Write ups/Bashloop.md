##Bash Loop
**We found a program that is hiding a flag but requires you to guess the number it is thinking of. Chances are Linux has an easy way to try all the numbers... Go to /problems/f625672abc185c8d615f852c306d877f and try it out!**

>Hints:
>
>Either use SSH or use the Web Shell to get onto the shell server and navigate to the correct directory. Then do a quick Google search on 'bash loops'. You may need to use grep to filter out the responses as well!

Let's navigate to the problem drectory:

```bash
ssh user@shell2017.picoctf.com
cd /problems/f625672abc185c8d615f852c306d877f
ls
```

We have two files: bashloop and flag. We cannot do anything with flag due to a lack of permissions. We can, however, execute bashloop.

Executing bashloop gives us:

```
What number am I thinking of? It is between 0 and 4096
```

There is no prompt with this dialogue, suggesting we need to make a guess as an input parameter. 

Let's try it with 0:

```bash
./bashloop 0
```

We get :

```
Nope. Pick another number between 0 and 4096
```
Guessing all values will take too long, so instead we can code up a script to do it for us.

```bash
#!/bin/bash
#-v: filter out search term
cd /problems/f625672abc185c8d615f852c306d877f
for i in `seq 1 4096`; do
        ./bashloop $i | grep -v "Nope"
        done
```

Executing this script `./bashloop.sh` gives us:

```
Yay! That's the number! Here be the flag: bcb04466bee8f895a789392ce8a09d13
```