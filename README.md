

# Jeddah landmarks and points of interest

## Executive summary

This is a map of interesting locations in and around Jeddah,
mainly aimed to be used and edited by the KAUST community,
although anyone is warmly welcomed to have a sneak peek
and to contribute as well.

### Desktop users
Open [the map](https://maps.google.com/?q=https://raw.githubusercontent.com/Virtakuono/.kml-repository/master/JeddahSaudiArabia.kml)
in a browser and explore. To avoid extra clutter, there are small submaps of the following regions
[Thuwal](https://maps.google.com/?q=https://raw.githubusercontent.com/Virtakuono/.kml-repository/master/submap_Thuwal.kml),
[Jeddah](https://maps.google.com/?q=https://raw.githubusercontent.com/Virtakuono/.kml-repository/master/submap_Jeddah.kml),
[Abha](https://maps.google.com/?q=https://raw.githubusercontent.com/Virtakuono/.kml-repository/master/submap_Abha.kml),
[Taif](https://maps.google.com/?q=https://raw.githubusercontent.com/Virtakuono/.kml-repository/master/submap_Taif.kml).

### Smartphone, tablet, etc. users

Unfortunately, opening the map on a smartphone or a tablet can be a bit more subtle
and depends on which device and browser is being used and what apps have been installed.
So far only Apple/Windows devices have been tested.
If you are able (and you should be) to open the map on an android or
or blackberry or whatever gizmo, please tell us how you did it: juho.happola@iki.fi
For the time being, the Apple and WP instructions are the only ones available:

#### Apple iOS

The essential data is stored in a .kml file that can be opened in two ways.
  1. In browser. This is probably the simplest way. Experience says that the best
     browser to view this map is using Safari. Open [this page](https://maps.google.com/?q=https://raw.githubusercontent.com/Virtakuono/.kml-repository/master/JeddahSaudiArabia.kml)
     in Safari and enjoy. If you open it in Google Chrome and you have Google Maps app installed,
     the browser will try to launch Google Maps App with devastating results.
  2. In an app such as Google Earth. This is the less simple way. First of all you have to have the app installed. Secondly
     you need to open [this file](https://raw.githubusercontent.com/Virtakuono/.kml-repository/master/JeddahSaudiArabia.kml)
     using that app. Unfortunately, if you click the link on a mobile device, you will likely have a bunch of code shown to you.
     The way around this is to download the file to a computer and to send it to yourself as an email attachment.
     Then, read your email using your mobile device and open the attachment. You should be offered a choice of apps to open it with,
     go for Google Earth.

#### Windows phone

  1. Open [this link](https://maps.google.com/?q=https://raw.githubusercontent.com/Virtakuono/.kml-repository/master/JeddahSaudiArabia.kml)
     to view the map.
  2. You may also download the [coordinates in the Nokia landmark exchange format](https://raw.githubusercontent.com/Virtakuono/.kml-repository/master/JeddahPOIs.lmx)
     (In testing).

## Longer readme

### What is this?

Essentially, this is an effort to bring back to life
[this map](https://maps.google.com/maps/ms?ie=UTF8&t=h&hl=en&vps=1&jsv=178b&safe=on&oe=UTF8&msa=0&msid=109723124894778733708.0004726ebc11f578c532c&dg=feature)
that has been left unedited for almost three years at the time of writing.
Later on other maps and other people have contributed to the contents
of this map overlay file and associated database. The goals are

  1. To provide geographical information in an usable form.
  2. To generate a revision history of the map while allowing
     the general audience to contribute to the contents.
  3. Maintain the geographical data in a format where
     pretty much anyone has access to the coordinate numbers
     in case the data needs to be transferred somewhere.

### How to contribute?

In order to add a new point of interest to the list,
no tech skills are needed. You only need to have access
to this 
[google spreadsheet](https://docs.google.com/spreadsheets/d/1-34A8wdzOaiz36Mnx74PbDsaRGTcCZP92rPLV9aP3fM/edit#gid=0),
to know the location of your point of interest
and add it to the sheet with a descriptive name and,
if possible, further instructions.

Unfortunately, getting the coordinates of your current whereabouts
*in a readable and useful format* might sometimes be a hassle. On iOS
one may use the
[Coordinates app](https://itunes.apple.com/us/app/coordinates-calculate-convert/id494286614?mt=8)
it allows to copy your current location onto pasteboard or to
send it in an email.

The data will not be automatically transferred to the map,
this is known feature to avoid erroneous edits.
To speed up the editorial process send an email to juho.happola@iki.fi. 

When editing the map please avoid the following common mistakes
  1. Assuming everyone knows you. In compiling this map I have had to do some forensics, maps like this tend to be
     copied from one source to another and statements like "This is the best yemeni restaurant I have been to" lose
     meaning when nobody knows who "I" is. Please consider leaving an identifying notification, initials, email address or
     a nickname.
  2. Spelling. Nothing gets transferred to the master map without a brief review. Please make this review a bit easier by
     avoiding excessive capitalisation, broken engrish and the like.
  3. Removing Points of Interest: Removing old and outdated info is as important (if not more important) as adding new ones.
     When one removes a line from the spreadsheet, it is often hard to distinguish whether this was
     an erroneous edit, vandalism or something that should be published. Thus, if you feel that there
     is a POI that should not be there, please go to the [spreadsheet](https://docs.google.com/spreadsheets/d/1-34A8wdzOaiz36Mnx74PbDsaRGTcCZP92rPLV9aP3fM/edit#gid=0)
     and write into the description section of the relevant POI something like:
     "This shop has been closed since May 2013" or "I was there, I did not see a camel souq",
     if possible, along with your initials, contact information or a nickname. Alternatively,
     send an email to complain.

Should you want to contribute code, icons, or add new types of
points of interest, I recommend you fork the repository, do your changes
and make a pull request.

#### Editing the KML file

Since the map essentially
relies on the github server to host the 
data contained in [a static .kml file](https://raw.githubusercontent.com/Virtakuono/.kml-repository/master/JeddahSaudiArabia.kml),
that contains the essential information of the map, note that
any changes need to be pushed to the server before they are
public. For debugging purposes you may
  1. view your edited .kml file locally in, for example, google earth
  2. put your kml file online somewhere (eg. Dropbox public folder) and modify the [gmail url](https://maps.google.com/?q=https://put.the.address.to.your.kml.file/here.kml) accordingly
  3. make changes while testing on a different branch than the master.

### (Partial) List of contents

  * [backup_kmls.py](https://github.com/Virtakuono/.kml-repository/blob/master/backup_kmls.py)
    This script is the centerpiece of the repository. Running it updates multiple files
    based on the Google Spreadsheet, which is downloaded in .ods and .tsv formats and
    processed into .kml and .lmx files. Furthermore, this script downloads the .kml files
    of maps being tracked and uses diff to see whether they have been changed.
  * [JeddahInterestedLocations.kml](https://github.com/Virtakuono/.kml-repository/blob/master/JeddahInterestedLocations.kml)
    Copy of the Jeddah: Interested locations -map for safekeeping
  * [JeddahInterestedLocations_old.kml](https://github.com/Virtakuono/.kml-repository/blob/master/JeddahInterestedLocations_old.kml)
    Old version of the file above, for diff
  * [JeddahPOIs.kml](https://github.com/Virtakuono/.kml-repository/blob/master/JeddahPOIs.kml)
    A .kml file automatically generated using backup_kmls.py based on the google spreadsheet. Often copied to JeddahSaudiArabia.kml
    after a review
  * [JeddahPOIs.lmx](https://github.com/Virtakuono/.kml-repository/blob/master/JeddahPOIs.lmx)
    and
    [JeddahPois_old.lmx](https://github.com/Virtakuono/.kml-repository/blob/master/JeddahPois_old.lmx)
    Same as the previous two files, but in .lmx format. Generated by backup_kmls.py
  * [JeddahPOIs.ods](https://github.com/Virtakuono/.kml-repository/blob/master/JeddahPOIs.ods)
    Copy of the google spreadsheet data in .ods format. This is downloaded automatically by
    running backup_kmls.py
  * [JeddahPOIs.tsv](https://github.com/Virtakuono/.kml-repository/blob/master/JeddahPOIs.tsv)
    and
    [JeddahPOIs_styles.tsv](https://github.com/Virtakuono/.kml-repository/blob/master/JeddahPOIs_styles.tsv)
    contain the Google spreadsheet data in .tsv format for the two first sheets.
  * [JeddahSaudiArabia.kml](https://github.com/Virtakuono/.kml-repository/blob/master/JeddahSaudiArabia.kml)
    The main file, containing the geographical data in .kml format for viewing by the general public.
    Edit with caution.
  * [JeddahShopping.kml](https://github.com/Virtakuono/.kml-repository/blob/master/JeddahShopping.kml)
    and
    [JeddahShopping_old.kml](https://github.com/Virtakuono/.kml-repository/blob/master/JeddahShopping_old.kml)
    contain a backup copy of the current and old version of Terry King's Jeddah Shopping map.
    These are updated by backup_kmls.py
  * [kmlgen.py](https://github.com/Virtakuono/.kml-repository/blob/master/kmlgen.py)
    a small script to generate a landmark in .kml format using command line.
  * [README.md](https://github.com/Virtakuono/.kml-repository/blob/master/README.md)
    This readme file, that serves as the root of this project.
  * [Thuwal.kml](https://github.com/Virtakuono/.kml-repository/blob/master/Thuwal.kml)
    and
    [Thuwal_old.kml](https://github.com/Virtakuono/.kml-repository/blob/master/Thuwal_old.kml)
    contain a copy of the current and previous version of the Thuwal map by Claire Sale.
  * [find_pin.sh](http://github.com/Virtakuono/.kml-repository/blob/master/find_pin.sh)
    a very, very small script to find geographical data from the Jeddah Interested Locations map
    kml file.
    [find_pin_shopping.sh](https://github.com/Virtakuono/.kml-repository/blob/master/find_pin_shopping.sh)
    and [find_pin_thuwal.sh](https://github.com/Virtakuono/.kml-repository/blob/master/find_pin_thuwal.sh)
    serve the same purpose for the Thuwal.kml and JeddahShopping.kml maps.
  * [gregs_abha_map.kml](https://github.com/Virtakuono/.kml-repository/blob/master/gregs_abha_map.kml)
    and
    [gregs_taif_map.kml](https://github.com/Virtakuono/.kml-repository/blob/master/gregs_taif_map.kml)
    contain maps that Greg Wickham kindly provided from his tours around the Kingdom.
  * [list_locations.sh](https://github.com/Virtakuono/.kml-repository/blob/master/list_locations.sh)
    lists all the landmarks in the three .kml files being tracked and outputs them
    in stdout with poor formatting.
  * [submap_Abha.kml](https://github.com/Virtakuono/.kml-repository/blob/master/submap_Abha.kml),
    [submap_Taif.kml](https://github.com/Virtakuono/.kml-repository/blob/master/submap_Taif.kml),
    [submap_Riyadh.kml](https://github.com/Virtakuono/.kml-repository/blob/master/submap_Riyadh.kml) and
    [submap_Thuwal.kml](https://github.com/Virtakuono/.kml-repository/blob/master/submap_Thuwal.kml)
    contain the same data as JeddahPOIs.kml, and are likewise generated by backup_kmls.py, only
    rectangular areas specific to each submap are selected to limit the number of landmarks and file
    size.
  * [Icons folder](https://github.com/Virtakuono/.kml-repository/tree/master/icons)
    contains all the icons needed for the .kml files as well a small
    [readme.txt](https://github.com/Virtakuono/.kml-repository/blob/master/icons/readme.txt)
    to help in creating more icons, when needed.

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
[Claire Sale](https://maps.google.com/maps/ms?msid=216110785410091998621.0004a4de8ab547c2ca385&msa=0&ll=22.287002,39.112723&spn=0.001437,0.001851&dg=feature),
Greg Wickham and professor Raul Tempone.
Thank you for helpful comments and corrections from Luca Passone and Idris Aija.

### License

Icons are copied from
[Map Icons Collection by Nicolas Mollet](http://mapicons.nicolasmollet.com)
under [CC BY SA 3.0 License](http://creativecommons.org/licenses/by-sa/3.0/)
the few shell scripts in this repository may be redistributed under the same
license, unless otherwise noted in the respective files.


