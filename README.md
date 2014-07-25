

# Jeddah landmarks and points of interest

## Executive summary

This is a map of interesting locations in and around Jeddah,
Kingdom of Saudi Arabia. If you just want to look at the map on a computer,
see [here](https://maps.google.com/?q=https://raw.githubusercontent.com/Virtakuono/.kml-repository/master/JeddahSaudiArabia.kml).

Unfortunately, if you are on a smartphone, the way to open this map
is a bit more subtle. The following ways have been tested:
  1. Open [this file](https://raw.githubusercontent.com/Virtakuono/.kml-repository/master/JeddahSaudiArabia.kml)
     using Apple Safari
  2. Open the file with whatever method, email it to yourself and then from your email inbox, choose to open
     the attachment using google maps app. Of course if you do not have google maps, you need to download it from the apple store.

Opening the map on windows or android phones has not been tested, if you have one of those phones
and would like to help, email juho.happola@iki.fi

## The longer version of the story

### What is this?

Essentially, this is an effort to bring back to life
[this map](https://maps.google.com/maps/ms?ie=UTF8&t=h&hl=en&vps=1&jsv=178b&safe=on&oe=UTF8&msa=0&msid=109723124894778733708.0004726ebc11f578c532c&dg=feature)
that has been left unedited for almost three years at the time of writing.

### How to contribute?

In case you want to edit to make improvements or correct errors,
please fork this repositoryand make pull request. In case you are
not willing to do this, you may read the instructions further for the
links to other maps and make edits to those maps, that will, after review,
<<<<<<< HEAD
be included into this repository in a semi-automated manner. As a third
option and last resort or in case of questions arise send an email
to juho.happola@iki.fi.

=======
be included into this repository in a semi-automated manner.
The repository also contains tools to automatically generate the relevant
map files based on the contents of a [google spreadsheet](https://docs.google.com/spreadsheets/d/1-34A8wdzOaiz36Mnx74PbDsaRGTcCZP92rPLV9aP3fM/edit#gid=0)
that can be edited by anyone. 
As a fourth
option and last resort or in case of questions arise send an email
to juho.happola@iki.fi.

When editing the map please avoid the following common mistakes
  1. Assuming everyone knows you. In compiling this map I have had to do some forensics, maps like this tend to be
     copied from one source to another and statements like "This is the best yemeni restaurant I have been to" lose
     meaning when nobody knows who "I" is. Please consider leaving an identifying notification, initials, email address or
     a nickname.
  2. Spelling. Nothing gets transferred to the master map without a brief review. Please make this review a bit easier by
     avoiding excessive capitalisation, broken engrish and the like.

>>>>>>> debug
#### Editing the KML file

Since the map essentially
relies on the github server to host the [JeddahSaudiArabia.kml file](https://raw.githubusercontent.com/Virtakuono/.kml-repository/master/JeddahSaudiArabia.kml),
that contains the essential information of the map, note that
any changes need to be pushed to the server before they are
public. For debugging purposes you may
  1. view your edited .kml file locally in, for example, google earth
  2. put your kml file online somewhere (eg. Dropbox public folder) and modify the [gmail url](https://maps.google.com/?q=https://put.the.address.to.your.kml.file/here.kml) accordingly
  3. make changes while testing on a different branch than the master.

### Credits, acknowledgements

There are a plethora of google maps that have roughly the
same purpose as this map and credit to most of the contents in
this map belongs to the people who have initiated and maintained
those maps.
Many of those maps appear to have
been copied from the same source and as they are
assumably not subject to copyright, 
geographical data has been copied from both of them rather
ruthlessly. 
Two maps especially worth mentioning are
[Jeddah: Interested Locations](https://maps.google.com/maps/ms?msid=203555040976874160945.0004cf9d6a73b19256e5f&msa=0&ll=20.694462,41.31958&spn=4.983057,8.448486&dg=feature)
and
[Jeddah Shopping](https://maps.google.com/maps/ms?ie=UTF8&msa=0&msid=114277812997999651227.0004863c2f62b04789ee3&ll=21.487734,39.203382&spn=0.009803,0.021007&t=h&z=16&iwloc=000486d78d6a0da7a66b9&dg=feature) by Terry King.
The first one is a rather comprehensive list of items, but lacks
version control. Anyone can edit and as there is no version control,
any fat finger mistakes are nearly impossible to correct.
The latter one, on the other hand, is more correct, but the only
option to edit it is through emailing the author.
This map aims to fix the problems by
  1. Creating a backup and version control of both of the maps mentioned above in order to track how these maps have been edited
  2. Allowing non-git-users to make changes to the former map in a way that is easy to update into the relevant .kml file.

In addition to the two maps mentioned above, this repository
includes material from
[Claire Sale](https://maps.google.com/maps/ms?msid=216110785410091998621.0004a4de8ab547c2ca385&msa=0&ll=22.287002,39.112723&spn=0.001437,0.001851&dg=feature)
and professor Raul Tempone.

### License

Icons are copied from
[Map Icons Collection by Nicolas Mollet](http://mapicons.nicolasmollet.com)
under [CC BY SA 3.0 License](http://creativecommons.org/licenses/by-sa/3.0/)
the few shell scripts in this repository may be redistributed under the same
license, unless otherwise noted in the respective files.


