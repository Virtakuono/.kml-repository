

# Jeddah landmarks and points of interest

## Executive summary

This is a map of interesting locations in and around Jeddah,
mainly aimed to be used and edited by the KAUST community,
although anyone is warmly welcomed to have a sneak peek
and to contribute as well.

### Viewing

Open <a href="https://rawgit.com/Virtakuono/.kml-repository/master/JeddahPOIs.htm" target="_blank">the map</a>.
This should work on desktops, cellphones, tablets and whatever gizmos and is the recommended way.

#### Alternate methods.

If you want to view the POIs using some alternate methods, the following are provided:

##### .kml Overlays on google maps:
<a href="https://maps.google.com/?q=https://raw.githubusercontent.com/Virtakuono/.kml-repository/master/JeddahSaudiArabia.kml" target="_blank">All data</a>
<a href="https://maps.google.com/?q=https://raw.githubusercontent.com/Virtakuono/.kml-repository/master/submap_Thuwal.kml" target="_blank">Thuwal</a>,
<a href="https://maps.google.com/?q=https://raw.githubusercontent.com/Virtakuono/.kml-repository/master/submap_Jeddah.kml" target="_blank">Jeddah</a>,
<a href="https://maps.google.com/?q=https://raw.githubusercontent.com/Virtakuono/.kml-repository/master/submap_Abha.kml" target="_blank">Abha</a> and
<a href="https://maps.google.com/?q=https://raw.githubusercontent.com/Virtakuono/.kml-repository/master/submap_Taif.kml" target="_blank">Taif</a>.

##### Nokia .lmx format 

This is experimental, but you may load the
<a href="https://raw.githubusercontent.com/Virtakuono/.kml-repository/master/JeddahPOIs.lmx" target="_blank">data in .lmx</a> format too:

## Longer readme

### What is this?

Essentially, this is an effort to bring back to life
<a href="https://maps.google.com/maps/ms?ie=UTF8&t=h&hl=en&vps=1&jsv=178b&safe=on&oe=UTF8&msa=0&msid=109723124894778733708.0004726ebc11f578c532c&dg=feature" target="_blank">this map</a>
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

#### Add a point using a map

Go to the <a href="https://rawgit.com/Virtakuono/.kml-repository/master/JeddahPOIs.htm" target="_blank">the map</a>,
zoom into the place where you want to add a point. Click on the map and follow the instructions on the popup.

#### Add a point whose coordinates you know

Add a new point of interest: go to
<a href="https://docs.google.com/spreadsheets/d/1-34A8wdzOaiz36Mnx74PbDsaRGTcCZP92rPLV9aP3fM/edit#gid=0" target="_blank">
the google spreadsheet
</a>, copy a row of data and make a duplicate of it.
Edit the duplicated row by writing the appropriate
name, description and coordinates.

#### Add a point using a photo you have taken

If you have a photo you have taken with a smartphone in an interesting location,
please send it to
<a href="mailto:juho.happola@iki.fi?Subject=POI%20hint">us</a>.
Add a description of what is in there and we'll extract the coordinates.
Please use the poorest quality settings, as the picture is not used
for anything anyways.

#### Other

Other complaints and corrections can be emailed to 
<a href="mailto:juho.happola@iki.fi?Subject=POI%20hint">us</a>.

#### Remember

The data will not be automatically transferred to the map,
this is known feature to avoid erroneous edits.
To speed up the editorial process send us an email.

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
     is a POI that should not be there, please go to the spreadsheet
     and write into the description section of the relevant POI something like:
     "This shop has been closed since May 2013" or "I was there, I did not see a camel souq",
     if possible, along with your initials, contact information or a nickname. Alternatively,
     send an email to complain.
  4. Coordinate systems. 
     If you have coordinates in degrees, minutes and seconds, please go to 
     the coordinate transformation tab on the spreadsheet and enter the
     archaic coordinates to transform them into more modern ones.

Should you want to contribute code, icons, or add new types of
points of interest, I recommend you fork the repository, do your changes
and make a pull request.

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
been copied from the same source. The material
has been screened as well as possible and the relevant bits
included after careful review in the new map.
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
Greg Wickham, Aya Rae, Grace Gruendler and professor Raul Tempone.
Thank you for helpful comments and corrections from Idris Aija, and Luca Passone.

### License

Icons are copied from
[Map Icons Collection by Nicolas Mollet](http://mapicons.nicolasmollet.com)
under [CC BY SA 3.0 License](http://creativecommons.org/licenses/by-sa/3.0/)
the few shell scripts in this repository may be redistributed under the same
license, unless otherwise noted in the respective files.
In addition, the open street map overlays use [leaflet library](http://leafletjs.com/) by Vladimir Agafonkin
and CloudMade and [providers plugin](https://github.com/leaflet-extras/leaflet-providers).
Leaflet is subject to its [own license](https://github.com/Leaflet/Leaflet/blob/master/LICENSE)


