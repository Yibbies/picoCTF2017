<h1>Digital Camouflage</h1>
**We need to gain access to some routers. Let's try and see if we can find the password in the captured network data.**

>Hints:

>- It looks like someone logged in with their password earlier. Where would log in data be located in a network capture?
>- If you think you found the flag, but it doesn't work, consider that the data may be encrypted.

Quick look at the captured traffic suggests that any transactions will occur over HTTP (other protocols present typically do not deal with transactions that require passwords).

Since we're focussing on HTTP, we are most probably looking for a POST packet.

There are many ways to search for a POST packet. One of the most direct ways is to filter them out. This can be done by typing the following term into Wireshark's filter:

```html
http.request.method == POST
```

This filters out all but one packet. Analysis of this packet reveals it is submitting credentials for a webform. We are able to pull these credentials out to obtain:

```
userid: curlinga
pswrd: dEo2NFpxYmRMdw==
```

Since we're only interested in the password we will focus on pswrd.

Based on the format (containing two == at the end) we can assume this password is encrypted in base64. Therefore, we can just search for an online tool to decrypt it for us (https://www.base64decode.org/).

Doing just that we get the password (and flag) as: 

```
tJ64ZqbdLw
``` 

