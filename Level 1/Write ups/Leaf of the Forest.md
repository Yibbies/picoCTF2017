<h1>Leaf of the Forest</h1>
**We found an even bigger directory tree hiding a flag starting at /problems/b88cc963bcaf6042d143bfef6db2100b. It would be impossible to find the file named flag manually...**

>Hints:
>
>Is there a search function in Linux? Like if I wanted to 'find' something...

Navigate to the problem directory. Here we have a directory called forest. Moving into the directory we get a lot of trees. 

```bash
cd forest
ls
```

Not even going to try....Lets go back one level outside the forest


```bash 
cd ..
```

Lets just search for a flag:

```bash
#. means current directory
find . | grep flag
```

Executing the find command, we get:

```
./forest/.../branchc96e/flag
```

Using cat on the full path:

```bash
cat ./forest/.../branchc96e/flag
```

Gives us the flag:

```
eb34ff576412f11b06fb68884bef0ec5
```
