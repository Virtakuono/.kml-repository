#!/usr/bin/python

import PIL.Image
import PIL.ExifTags
import sys

img = PIL.Image.open(sys.argv[1])
exif = {PIL.ExifTags.TAGS[k]: v for k,v in img._getexif().items() if k in PIL.ExifTags.TAGS}

g = exif['GPSInfo']

latlon = [1.0,1.0]
latlon[0] *= g[2][0][0]/float(g[2][0][1])
latlon[0] += g[2][1][0]/float(g[2][1][1]*60)
latlon[0] += g[2][2][0]/float(g[2][2][1]*3600)
latlon[1] *= g[4][0][0]/float(g[4][0][1])
latlon[1] += g[4][1][0]/float(g[4][1][1]*60)
latlon[1] += g[4][2][0]/float(g[4][2][1]*3600)

if not (g[1] == 'N'):
    latlon[0] *= -1

if not (g[3] == 'E'):
    latlon[1] *= -1

print('The coordinates of the picture %s are (%.7f,%.7f).'%(sys.argv[1],latlon[0],latlon[1]))
