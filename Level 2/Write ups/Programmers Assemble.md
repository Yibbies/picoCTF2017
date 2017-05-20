<h1>Programmers Assemble</h1>
**You found a text file with some really low level code. Some value at the beginning has been X'ed out. Can you figure out what should be there, to make main return the value 0x1? Submit the answer as a hexidecimal number, with no extraneous 0s. For example, the decimal number 2015 would be submitted as 0x7df, not 0x000007df**

>Hints:
>
>- All of the commands can be found here along with what they do.
>- It may be useful to be able to run the code, with test values.

We are given the following assembly source code. 

```assembly
.global main

main:
    mov $XXXXXXX, %eax
    mov $0, %ebx
    mov $0x5, %ecx
loop:
    test %eax, %eax
    jz fin
    add %ecx, %ebx
    dec %eax
    jmp loop
fin:
    cmp $0x7ee0, %ebx
    je good
    mov $0, %eax
    jmp end
good:
    mov $1, %eax
end:
    ret
```

Translating the code into something a bit more readable gives us:

```
main 
	a = x //What is the value of x?
	b = 0
	c = 5
	
	while(a!=0) 
		b+=c
		a--
	return fin

fin
	if(b==0x7ee0) //32480
		return good
	a = 0
	return end

good
	a = 0x1
	return a

end
	return
```
After converting 0x7ee0 from hexadecimal to decimal to get 32480. We can see the goal here is to set a so that the while loop repeats enough times for b to equal 32,480. Since b increases by the value of c, we conclude that the loop needs to repeat 6496 times. Converting 6496 to hex gives us a value of 1960. Thus our flag is:

```
0x1960
```