#!/usr/bin/python

import sys

head = '<Placemark>\n'
tail = '</Placemark>\n'
name = lambda foo: '    <name>%s</name>\n'%(foo,)
desc = lambda foo: '    <description><![CDATA[<div dir=\"ltr\">%s</div>]]></description>\n    <styleUrl>#style12</styleUrl>\n'%(foo,)
coord = lambda lon,lat: '    <Point>\n      <coordinates>%.7f,%.7f,%.7f</coordinates>\n    </Point>\n'%(lon,lat,0.0)
help = '\nA small helper script to generate a kml tag for a position.\nUsage:\n./kmlgen.py name description longitude latitude\n'
kmlfun = lambda foo,bar,baz,bat: '%s%s%s%s%s'%(head,name(foo),desc(bar),coord(baz,bat),tail)

try:
    kmlstring = kmlfun(sys.argv[1],sys.argv[2],float(sys.argv[3]),float(sys.argv[4]))

    print('\n\nadd the following to the .kml file:\n\n')
    print(kmlstring)

except IndexError:
    print(help)

