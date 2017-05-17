##keyz
**While webshells are nice, it'd be nice to be able to login directly. To do so, please add your own public key to ~/.ssh/authorized_keys, using the webshell. Make sure to copy it correctly! The key is in the ssh banner, displayed when you login remotely with ssh, to shell2017.picoctf.com**

>Hints:
>
>- There are plenty of tutorials out there. This one covers key generation: https://confluence.atlassian.com/bitbucketserver/creating-ssh-keys-776639788.html
>- Then, use the web shell to copy/paste it, and use the appropriate tool to ssh to the server using your key
>
This flag can be obtained by setting up ssh and using the host system's terminal instead of the webshell provided in the browser.

Follow the instructions to create a ssh public key. The key can be copied on to the server via the webshell using:

```bash
echo "public_key.pub text" >> ~/.ssh/authorized_keys
```

To ssh in and obtain the flag we type [user]@shell2017.picoctf.com in our hosts terminal.

Upon authentication we can see the flag in the ssh banner:

```
who_needs_pwords_anyways
```
