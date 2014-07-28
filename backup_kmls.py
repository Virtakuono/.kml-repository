#!/usr/bin/python

import sys
import os
import cgi

class POIStyle():

    def __init__(self,ID=684,icon='generic',type='N/A'):
        self.id = ID
        self.type = type
        self.icon = '%s.png'%(icon,)

    def __str__(self):
        rv = '        <href>https://raw.githubusercontent.com/Virtakuono/.kml-repository/master/icons/%s</href>\n'%(self.icon,)
        rv = '      <Icon>\n%s      </Icon>\n'%(rv,)
        rv = '    <IconStyle>\n%s    </IconStyle>\n'%(rv,)
        rv = '  <Style id=\"style%d\">\n%s  </Style>\n'%(self.id,rv)
        return rv

class POI():

    def __init__(self,name='POI',desc='N/A',lat=0.0,lon=0.0,type=POIStyle()):
        self.name = name
        self.type = type
        self.lat = lat
        self.lon = lon
        self.desc = desc

    def __str__(self):
        rv = '      <coordinates>%.7f,%.7f,%.7f</coordinates>\n'%(self.lon,self.lat,0.0)
        rv = '    <Point>\n%s    </Point>\n'%(rv,)
        rv = '    <styleUrl>#style%d</styleUrl>\n%s'%(self.type.id,rv)
        rv = '    <description><![CDATA[<div dir=\"ltr\">%s</div>]]></description>\n%s'%(cgi.escape(self.desc),rv)
        rv = '    <name>%s</name>\n%s'%(cgi.escape(self.name),rv)
        rv = '  <Placemark>\n%s  </Placemark>\n'%(rv,)
        return rv

    def lmxstr(self):
        rv = '  <lm:landmark>\n'
        rv += '    <lm:name>%s</lm:name>\n'%(cgi.escape(self.name),)
        rv += '    <lm:coordinates>\n'
        rv += '      <lm:latitude>%.6f</lm:latitude>\n'%(self.lat,)
        rv += '      <lm:longitude>%.6f</lm:longitude>\n'%(self.lon,)
        rv += '      <lm:altitude>0.0</lm:altitude>\n'
        rv += '    </lm:coordinates>\n'
        rv += '  </lm:landmark>\n'
        return rv

class POISet():
    
    def __init__(self,name='Points of Interest in and near Jeddah, Kingdom of Saudi Arabia',desc='See detailed info, licensing and instructions on how to contribute yourself at https://github.com/Virtakuono/.kml-repository#jeddah-landmarks-and-points-of-interest',filename='JeddahPOIs'):
        self.name = name
        self.desc = desc
        self.filename = filename
        filename = '%s_styles.tsv'%(self.filename,)
        file = open(filename)
        lines = file.readlines()
        file.close()
        self.styles = [POIStyle(ID=foo) for foo in range(1,1501)]
        for line in lines:
            if line[-1] == '\n':
                line = line[:-1]
                id = int(line[:line.find('\t')])
            line = line[line.find('\t')+1:]
            type = line[:line.find('\t')]
            line = line[line.find('\t')+1:]
            filename = line
            style = POIStyle(ID=id,icon=filename,type=type)
            self.styles[style.id] = style
        filename = '%s.tsv'%(self.filename,)
        file = open(filename)
        lines = file.readlines()
        file.close()
        lines = lines[1:]
        self.POIs = []
        for line in lines:
            if line[-1] == '\n':
                line = line[:-1]
            name = line[:line.find('\t')]
            line = line[line.find('\t')+1:]
            desc = line[:line.find('\t')]
            line = line[line.find('\t')+1:]
            lat = float(line[:line.find('\t')])
            line = line[line.find('\t')+1:]
            lon = float(line[:line.find('\t')])
            line = line[line.find('\t')+1:]
            line = line[line.find('\t')+1:]
            id  = int(line[:line.find('\t')])
            self.POIs.append(POI(name=name,desc=desc,lat=lat,lon=lon,type=self.styles[id]))
        effstyles = []
        for poi in self.POIs:
            if poi.type not in effstyles:
                effstyles.append(poi.type)
        self.styles = effstyles

    def __str__(self,):
        rv = '<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n'
        rv += '<kml xmlns=\"http://earth.google.com/kml/2.2\">\n'
        rv += '<Document>\n'
        rv += '  <name>%s</name>\n'%(self.name,)
        rv += '  <description><![CDATA[%s]]></description>\n'%(self.desc,)
        for style in self.styles:
            rv += style.__str__()
        for POI in self.POIs:
            rv += POI.__str__()
        rv += '</Document>\n'
        rv += '</kml>\n'
        return rv

    def lmxstr(self,):
        rv = '<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>\n'
        rv += '<lm:lmx xmlns:lm=\"http://www.nokia.com/schemas/location/landmarks/1/0\">\n'
        rv += ' <lm:landmarkCollection>\n'
        rv += ' <lm:name>%s</lm:name>\n'%(self.name,)
        rv += ' <lm:description>%s</lm:description>\n'%(self.desc)
        for POI in self.POIs:
            rv += POI.lmxstr()
        rv += ' </lm:landmarkCollection>\n'
        rv += '</lm:lmx>\n'
        return rv

    def writekml(self,fn='JeddahPOIs.kml'):
        file = open(fn,'w')
        file.writelines(self.__str__())
        file.close()

    def writelmx(self,fn='JeddahPOIs.lmx'):
        file = open(fn,'w')
        file.writelines([self.lmxstr(),])
        file.close()

class POISet_rectangle(POISet):

    def __init__(self,name='A submap',mastermap=POISet(),minlat=-90.0,maxlat=90.0,minlon=-180.0,maxlon=180.0,desc=''):
        self.name = name
        self.desc = desc
        self.POIs = []
        for POI in mastermap.POIs:
            if POI.lat > minlat:
                if POI.lat < maxlat:
                    if POI.lon < maxlon:
                        if POI.lon> minlon:
                            self.POIs.append(POI)
        self.styles = [style for style in mastermap.styles]
        effstyles = []
        for poi in self.POIs:
            if poi.type not in effstyles:
                effstyles.append(poi.type)
        self.styles = effstyles
        

class trackedMap():
    
    def __init__(self,name,url,filename):
        self.name = name
        self.url = url
        self.filename = filename

def main():
    print('Downloading google docs sheet...')
    os.system('wget -q -O JeddahPOIs.ods \"https://docs.google.com/spreadsheets/d/1-34A8wdzOaiz36Mnx74PbDsaRGTcCZP92rPLV9aP3fM/export?hl=en&exportFormat=ods\"')
    os.system('wget -q -O JeddahPOIs.tsv \"https://docs.google.com/spreadsheets/d/1-34A8wdzOaiz36Mnx74PbDsaRGTcCZP92rPLV9aP3fM/export?hl=en&exportFormat=tsv\"')
    os.system('wget -q -O JeddahPOIs_styles.tsv \"https://docs.google.com/spreadsheets/d/1-34A8wdzOaiz36Mnx74PbDsaRGTcCZP92rPLV9aP3fM/export?hl=en&exportFormat=tsv&gid=1132721881\"')
    print('Done.')
    print('Generating kml and lmx files...')
    poiSet = POISet()
    os.system('cp ./JeddahPOIs.kml ./JeddahPOIs_old.kml')
    os.system('cp ./JeddahPOIs.lmx ./JeddahPois_old.lmx')
    poiSet.writekml()
    poiSet.writelmx()
    print('Done.')
    print('Difference between old and new kml file:')
    os.system('diff ./JeddahPOIs.kml ./JeddahPOIs_old.kml')

    print('Generating submaps...')

    smcs = (('Thuwal',(22.2,22.3,39.1,39.2)),('Jeddah',(21.35,21.72,39.05,39.32)),('Taif',(21.16,21.5,40.17,40.61)),('Abha',(18.01,18.32,42.36,42.8)),('Riyadh',(24.5,24.94,46.36,47.0)))

    for foo in smcs:
        smName = 'Submap of JeddahPOIs: %s'%(foo[0],)
        smDesc = poiSet.desc
        smFilename = 'submap_%s.kml'%(foo[0])
        smObject = POISet_rectangle(mastermap=poiSet,minlat=foo[1][0],maxlat=foo[1][1],minlon=foo[1][2],maxlon=foo[1][3],name=smName,desc=smDesc)
        smObject.writekml(fn = smFilename)
    print('Done.')
    
    trackedMaps = [trackedMap('Jeddah: Interested locations','https://maps.google.com/maps/ms?dg=feature&ie=UTF8&authuser=0&msa=0&output=kml&msid=203555040976874160945.0004cf9d6a73b19256e5f','JeddahInterestedLocations')]
    trackedMaps += [trackedMap('Jeddah Shopping','https://maps.google.com/maps/ms?ie=UTF8&t=h&dg=feature&authuser=0&msa=0&output=kml&msid=203537519255214459478.0004863c2f62b04789ee3','JeddahShopping')]
    trackedMaps += [trackedMap('Thuwal map by Claire','https://maps.google.com/maps/ms?hl=en&ie=UTF8&oe=UTF8&dg=feature&authuser=0&msa=0&output=kml&msid=216110785410091998621.0004a4de8ab547c2ca385','Thuwal')]

    for map in trackedMaps:
        print('Downloading %s ...'%(map.name,))
        os.system('mv ./%s.kml ./%s_old.kml'%(map.filename,map.filename))
        os.system('wget -q -O %s.kml \"%s\"'%(map.filename,map.url))
        print('Done.')
        print('Diff of the old and new files:')
        os.system('diff ./%s.kml ./%s_old.kml'%(map.filename,map.filename))
    
    print('Do necessary changes, commit and push, if needed.')
    print('Goodbye')
        
main()
