<h1>Leaf of the Tree</h1>
**We found this annoyingly named directory tree starting at /problems/e9c1c685270e96936e44ad5768f23ce3. It would be pretty lame to type out all of those directory names but maybe there is something in there worth finding? And maybe we dont need to type out all those names...? Follow the trunk, using cat and ls!**

>Hints:
>
>Tab completion is a wonderful, wonderful thing

Navigate to the problem directory. Here we have a directory called trunk. Moving into the directory we get another trunk. 

```bash
cd trunk
ls
```

Moving into that we get a branch and another trunk.

```bash
cd trunk60a9
ls
```

Too tedious.

Lets go back to the first trunk.

```bash 
cd ../..
```

Lets just search for a flag:

```bash
#. means current directory
find . | grep flag
```

Executing the find command, we get:

```
./trunk/.../trunka18f/flag
```

Using cat on the full path:

```bash
cat ./trunk/.../trunka18f/flag
```

Gives us the flag:

```
b0e641edaceaa42e4d77e9f465516fdf
```
