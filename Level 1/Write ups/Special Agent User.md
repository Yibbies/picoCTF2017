<h1>Special Agent User</h1>
**We can get into the Administrator's computer with a browser exploit. But first, we need to figure out what browser they're using. Perhaps this information is located in a network packet capture we took: data.pcap. Enter the browser and version as "BrowserName BrowserVersion". NOTE: We're just looking for up to 3 levels of subversions for the browser version (ie. Version 1.2.3 for Version 1.2.3.4) and ignore any 0th subversions (ie. 1.2 for 1.2.0)**

>Hints:
>
>Where can we find information on the browser in networking data? Maybe try reading up on user-agent strings.

We immedietely know what we're looking for: the browser used and it's version. This information can be pulled from the user agent values, which are recorded in the packet metadata. We can filter these out using the following filter term:

```
http.user_agent
```

Using this filter, we get 7 packets to analyse. Unfortunetly, it is tricky to refine the results further without being too specific, running the risk of filtering out what we want accidently. Consequently, we are forced to look at each one manually.

Expanding the HTTP field we can see more details; specifically, the user agent string value. For most of the packets the user agent just says "Wget/1.16 (linux-gnu)". However, for one packet the user agent reads:

```
Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)
Chrome/36.0.1985.67 Safari/537.36
```

This user agent string contains information of four browsers. Referring back to the question, we are tasked at finding the browser with a subversion containing at least 3 levels (excluding zeros). The only browser listed matching that condition is Chrome. Thus our flag here is:

```
Chrome 36.0.1985.67
```