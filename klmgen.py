#!/usr/bin/python

import sys

head = '<Placemark>\n'
tail = '</Placemark>\n'
name = lambda foo: '    <name>%s</name>\n'%(foo,)
desc = lambda foo: '    <description><![CDATA[<div dir=\"ltr\">%s</div>]]></description>\n    <styleUrl>#style12</styleUrl>\n'%(foo,)
coord = lambda lon,lat: '    <Point>\n      <coordinates>%.7f,%.7f,%.7f</coordinates>\n    </Point>\n'%(lon,lat,0.0)

kmlstring = '%s%s%s%s%s'%(head,name(sys.argv[1]),desc(sys.argv[2]),coord(float(sys.argv[3]),float(sys.argv[4])),tail)

print('add the following to the .kml file:\n\n')
print(kmlstring)

