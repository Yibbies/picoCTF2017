<h1>Connect The Wigle</h1>

<B>Identify the data contained within wigle and determine how to visualize it. Update 16:26 EST 1 Apr If you feel that you are close, make a private piazza post with what you have, and an admin will help out.</B>

>Hints:
>
>- Perhaps they've been storing data in a database. How do we access the information?
>- How can we visualize this data? Maybe we just need to take a step back to get the big picture?
>- Try zero in the first word of the flag, if you think it's an O.
>- If you think you're super close, make a private piazza post with what you think it is.

First we see what kind of file wigle is:

```bash
file wigle
```

We're told the file is a SQLite 3.x database file. We can read its contents using DB Browser (https://github.com/sqlitebrowser/sqlitebrowser/wiki).

Importing wigle into the program gives us data on three tables:

1. android_metadata
2. location
3. network

Navigate to the browse data tab to view table data. Not much to look at in the android_metadata table. Lets look at location next. There are a bunch of fields that shows where and where various access points were discovered in 3D space. The networks table is similar in nature, in fact it appears the tables share a key and thus are linked (the main difference being that there are names associated with the various access points). 

We're told to see if we can visualise any data. In this situation, the best contenders would be the latitude and longitude of the data sets. As it turns out the coordinates in both tables are exactly the same (unsurprising since the tables are now assumed linked). So now we just need a way to visualise coordinates.

Google again provides us the solution: https://www.darrinward.com/lat-long/. We copy all the coordinate information and plot them using the website tool. We're given a bunch of markers that don't look like much. Lets zoom in. 

As we zoom in, the markers begin to look like characters. Interpreting the markers gives us our flag:

```
FLAG{F0UND_M3_EE263B5F}
```