##What Is Web
**Someone told me that some guy came up with the "World Wide Web", using "HTML" and "stuff". Can you help me figure out what that is? Website.**

>Hints:
>
>How can you figure out how the webpage is actually built?

We follow the link to the website (follow the other link for an optional history lesson). There we are presented with some text and an image. The use of tags suggests that the page is written in html or php. No matter the case, we can look at it's structure by selecting "inspect" from the context menu.

Inspecting the page immedietely tells us the page is written in html. Further scrutiny reveals part of a flag in the comments: 

```html
<!-- Cool! Look at me! This is an HTML file. It describes what each page 
		contains in a format your browser can understand. -->
<!-- The first part of the flag (there are 3 parts) is 72b28b258d2 -->
<!-- What other types of files are there in a webpage? -->
```
So we have part 1 out of 3 of the flag. The comments tells us to look at other files incorporated into the webpage.

If we select the "sources" tab from the inspect window's dock we can see a list of files which make up this webpage.

Currently we're looking at index (the front page), moving down the list to scrpt.js we find the next part of the flag:

```javascript
/* This is a javascript file. It contains code that runs locally in your
 * browser, although it has spread to a large number of other uses.
 *
 * The final part of the flag is ddd5020451d
 */
```

So now we have parts 1 and 3. 

Lets look at another file, hacker.css.

```css
/*
This is the css file. It contains information on how to graphically display
the page. It is in a seperate file so that multiple pages can all use the same 
one. This allows them all to be updated by changing just this one.
The second part of the flag is b2ea021486f 
*/
```

Located part 2. Now we have all three parts of the flag. Putting them together gives us our flag:

```
72b28b258d2b2ea021486fddd5020451d
```
