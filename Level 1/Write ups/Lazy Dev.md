##MASTER CHALLENGE (Lazy Dev)
**I really need to login to this website, but the developer hasn't implemented login yet. Can you help?**

>Hints:
>
>- Where does the password check actually occur?
>- Can you interact with the javascript directly?

Open the website. Just a password form and submit button. Without a means to enter a username, we can just skip over trying to brute force the password. In an attempt to see what this password page is meant to be used for we can inspect it's structure. We do this by opening the context menu and selecting "inspect".

Here we see the structure of the web form. We can see that the submit button has a function associated with it for when it is clicked. 

```html
<button type="button" onclick="process_password()">Submit</button>
```
Lets find this process\_password() function. Select Sources from the inspect window's dock. Here we see the files associated with the webpage. Expanding the static folder we can see the client.js file. At the bottom of the client.js file we see the process\_password() function, so we know we're in the right place. Reading the code we can backtrack the sequence of function calls which allows any password entered in the web form to be processed, but more likely we will forget all this when we see the validate() function:

```javascript
//Validate the password. TBD!
function validate(pword){
  //TODO: Implement me
  return false;
}
```
The developer of the webpage has not implemented the validation function. Since it returns false, no matter the password entered in the web form, it will always report that the password is invalid. If it always reports false, why don't we just swap it to make it always report true. Replace the false with true:

```javascript
//Validate the password. TBD!
function validate(pword){
  //TODO: Implement me
  return true; //change false to true
}
```
Save the file and lets hit the submit button:

```
client_side_is_the_dark_sidee5dbd5f8c6ae5e282766571e06569d50
```
We got our flag.