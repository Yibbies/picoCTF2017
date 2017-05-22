<h1>Coffee</h1>

<B>You found a suspicious USB drive in a jar of pickles. It contains this file file.</B>

>Hints:
>
>Is there a way to get the source of the program?

Class files are generally compiled java code. Lets just confirm it:

```bash
file freeThePickles.class
```
We get:
`freeThePickles.class: compiled Java class data, version 52.0 (Java 1.8)`

So it's a java class compiled in Java version 1.8.

Lets pull the source code. http://www.javadecompilers.com/ is a handy tool for this. Decompiling the code we get:

```java
import java.util.Base64.Decoder;

public class problem {
  public problem() {}
  
  public static String get_flag() { String str1 = "Hint: Don't worry about the schematics";
    String str2 = "eux_Z]\\ayiqlog`s^hvnmwr[cpftbkjd";
    String str3 = "Zf91XhR7fa=ZVH2H=QlbvdHJx5omN2xc";
    byte[] arrayOfByte1 = str2.getBytes();
    byte[] arrayOfByte2 = str3.getBytes();
    byte[] arrayOfByte3 = new byte[arrayOfByte2.length];
    for (int i = 0; i < arrayOfByte2.length; i++)
    {
      arrayOfByte3[i] = arrayOfByte2[(arrayOfByte1[i] - 90)];
    }
    System.out.println(java.util.Arrays.toString(java.util.Base64.getDecoder().decode(arrayOfByte3)));
    return new String(java.util.Base64.getDecoder().decode(arrayOfByte3));
  }
  
  public static void main(String[] paramArrayOfString) {
    System.out.println("Nothing to see here");
  }
}
```

So the code is actually for the problem class. We can also see that our flag is compiled together by catenating three String variables together and decoding them in base64. 

This is done by calling the get_flag() method. We also notice that the method has two products:

1. array of decoded base64 values
2. String decoded in base64

Since the first product will just give us numbers, we probably cannot do much with them. So we assigned the return value of the get_flag() method to a variable and print that off. Implemented these changes changes the code like so:

```java
public static void main(String[] paramArrayOfString) {
System.out.println("Nothing to see here");
System.out.println(get_flag());
}
```

Compiling and running the modified source code:

```bash
javac problem.java
java problem
```

Gives us our flag:

```
flag_{pretty_cool_huh}
```