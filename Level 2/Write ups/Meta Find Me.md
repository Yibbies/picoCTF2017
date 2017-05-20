<h1>Meta Find Me</h1>
**Find the location of the flag in the image: image.jpg. Note: Latitude and longitude values are in degrees with no degree symbols,/direction letters, minutes, seconds, or periods. They should only be digits. The flag is not just a set of coordinates - if you think that, keep looking!**

>Hints:
>
>How can images store location data? Perhaps search for GPS info on photos.

We are given the following image:

![](../Meta\ Find\ Me.jpg)

Since we're looking for GPD information, we should look into the EXIF data of the  image. Opening the properties of the image (Preview -> Tools -> Show Location Info on MacOS) gives us a latitude of 70$\circ$ and a longitude of 73$\circ$.

However entering these as the flag gives us a negative response. Have to look elsewhere. Another place to look for meta information is in the image's headers. We can view this using Hexfiend.

Scrolling down past all the hexadecimal chunks, we eventually find:

```
flag_2_meta_4_me_<lat>_<lon>_978a
```

We complete our flag by substituting in our previously found latitude and longitude coordinates.

```
flag_2_meta_4_me_70_73_978a
```