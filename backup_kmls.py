#!/usr/bin/python

import sys
import os
import cgi
import urllib2
import datetime
import time
import mgrs

class POIStyle():

    def __init__(self,ID=684,icon='generic',type='N/A'):
        self.id = ID
        self.ttype = type
        self.icon = '%s.png'%(icon,)

    def iconUrl(self):
        return 'https://raw.githubusercontent.com/Virtakuono/.kml-repository/master/icons/%s'%(self.icon,)

    def __str__(self):
        rv = '        <href>%s</href>\n'%(self.iconUrl(),)
        rv = '      <Icon>\n%s      </Icon>\n'%(rv,)
        rv = '    <IconStyle>\n%s    </IconStyle>\n'%(rv,)
        rv = '  <Style id=\"style%d\">\n%s  </Style>\n'%(self.id,rv)
        return rv

    def osmIconType(self):
        return 'iconType%d'%(self.id,)

    def osmhtmlstr(self):
        th = lambda i: 'iconType%d'%(i,)
        rv = '   var %s = L.icon({\n   iconUrl: \'%s\',\n   iconSize: [32,37],\n   iconAnchor: [16,37],\n   popupAnchor: [0,-20]\n   });\n'%(self.osmIconType(),self.iconUrl())
        return rv

class POI():

    def __init__(self,name='POI',desc='N/A',lat=0.0,lon=0.0,type=POIStyle()):
        self.name = name
        self.ttype = type
        self.lat = lat
        self.lon = lon
        self.desc = desc

    def osmUrl(self):
        return 'http://www.openstreetmap.org/?mlat=%.7f&mlon=%.7f&zoom=12&layers=M'%(self.lat,self.lon)

    def gmapUrl(self):
        return 'http://maps.google.com/maps?q=%7f,%.7f'%(self.lat,self.lon)

    def bingUrl(self):
        return 'http://www.bing.com/maps/?v=2&cp=%.8f~%.8f&lvl=16&dir=0&sty=c&sp=point.%.8f_%.8f_%s'%(self.lat,self.lon,self.lat,self.lon,urllib2.quote(self.name))

    def __str__(self):
        rv = '      <coordinates>%.7f,%.7f,%.7f</coordinates>\n'%(self.lon,self.lat,0.0)
        rv = '    <Point>\n%s    </Point>\n'%(rv,)
        rv = '    <styleUrl>#style%d</styleUrl>\n%s'%(self.ttype.id,rv)
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

    def htmlCoords(self):
        latC = 'N'
        lonC = 'E'
        if self.lat < 0.0:
            latC = 'S'
        if self.lon < 0.0:
            lonC = 'W'
        return '%.8f &deg; %s, %.8f &deg; %s'%(abs(self.lat),latC,abs(self.lon),lonC)

    def osmhtmlliststr(self,num):
        m = mgrs.MGRS()
        if not num:
            rv = '   <p>%s'%(self,name)
        else:
            rv = '   <p>%d. %s'%(num,self.name,)
        if self.desc:
            rv += ' - %s - \n'%(self.desc,)
        else:
            rv += ' - \n'
        rv += '   %s - %s -'%(self.htmlCoords(),m.toMGRS(self.lat,self.lon)) 
        rv += '   <a href=\"%s\">OSM</a>, <a href=\"%s\">Google maps</a>, <a href=\"%s\">Bing</a></p>\n'%(self.osmUrl(),self.gmapUrl(),self.bingUrl())
        return rv

    def osmhtmlstr(self):
        rv = '   L.marker([%.7f, %.7f],{icon: %s}).addTo(map).bindPopup(\"<b>%s</b><br />%s<br />Coordinates: (%.7f, %.7f)<br /><a href=\\"%s\\">OSM</a>, <a href=\\"%s\\">Google Maps</a>, <a href=\\"%s\\">Bing</a>\");\n'%(self.lat,self.lon,self.ttype.osmIconType(),self.name,self.desc,self.lat,self.lon,self.osmUrl(),self.gmapUrl(),self.bingUrl())
        rv = '   L.marker([%.7f, %.7f],{icon: %s}).bindPopup(\"<b>%s</b><br />%s<br />Coordinates: (%.7f, %.7f)<br /><a href=\\"%s\\">OSM</a>, <a href=\\"%s\\">Google Maps</a>, <a href=\\"%s\\">Bing</a>\").addTo(poilist);\n'%(self.lat,self.lon,self.ttype.osmIconType(),self.name,self.desc,self.lat,self.lon,self.osmUrl(),self.gmapUrl(),self.bingUrl())
        return rv

    def mdstr(self):
        return '###%s\n\n%s\n[osm](http://www.openstreetmap.org/?lat=%.7f&lon=%.7f)\n\n'

class POISet():
    
    def nowString(self,):
        # we want something like '2007-10-18 14:00+0100'
        mytz="%+4.4d" % (time.timezone / -(60*60) * 100) # time.timezone counts westwards!
        dt  = datetime.datetime.now()
        dts = dt.strftime('%Y-%m-%d %H:%M')  # %Z (timezone) would be empty
        nowstring="%s%s" % (dts,mytz)
        return nowstring

    def centerPoint(self):
        return (sum([POI.lat for POI in self.POIs])/float(len(self.POIs)), sum([POI.lon for POI in self.POIs])/float(len(self.POIs)))

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
            if poi.ttype not in effstyles:
                effstyles.append(poi.ttype)
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

    def osmhtmlstr(self,):

        layers = []

        codefun = lambda foo:  'var %s = L.tileLayer(\'%s\', {id: \'%s\', attribution: \'%s\'});\n\n'%(foo['id'],foo['url'],foo['id'],foo['attr'])

        p = {}
        p['id'] = 'OSM'
        p['name'] = 'OpenStreetMap: Mapnik'
        p['attr'] = 'Map data &copy; <a href=\"http://openstreetmap.org\">OpenStreetMap</a> contributors, '
        p['attr'] += '<a href=\"http://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>,'
        p['attr'] += 'Imagery &copy; <a href=\"http://openstreetmap.org\">OpenStreetMap</a>'
        p['url'] = 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'
        p['code'] = codefun(p)
        layers.append(p)

        p2 = {}
        p2['id'] = 'OSM2'
        p2['name'] = 'OpenStreetMap: Hydda'
        p2['attr'] = 'Map data &copy; <a href=\"http://openstreetmap.org\">OpenStreetMap</a> contributors, '
        p2['attr'] += '<a href=\"http://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>,'
        p2['attr'] += 'Imagery &copy; <a href=\"http://openstreetmap.org\">OpenStreetMap Sweden</a>'
        p2['url'] = 'http://{s}.tile.openstreetmap.se/hydda/full/{z}/{x}/{y}.png'
        p2['code'] = codefun(p2)
        layers.append(p2)

        p3 = {}
        p3['id'] = 'OCM'
        p3['name'] = 'OpenCycleMap: ThunderForest'
        p3['attr'] = 'Map data &copy; <a href=\"http://openstreetmap.org\">OpenStreetMap</a> contributors, '
        p3['attr'] += '<a href=\"http://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>,'
        p3['attr'] += 'Imagery &copy; <a href=\"http://opencyclemap.org\">OpenCycleMap</a>'
        p3['url'] = 'http://{s}.tile.thunderforest.com/cycle/{z}/{x}/{y}.png'
        p3['code'] = codefun(p3)
        layers.append(p3)


        p4 = {}
        p4['id'] = 'HERED'
        p4['name'] = 'HERE Street map'
        p4['attr'] = 'Map &copy; 1987-2014 <a href="http://developer.here.com">HERE</a>'
        p4['appid'] = 'NsbBYO9x9J3Ur21k1j8j'
        p4['appcode'] = 'p4GtVh8OBdi4zgGXw6RXCQ'
        p4['url'] =  'http://{s}.{base}.maps.cit.api.here.com/maptile/2.1/maptile/{mapID}/normal.day/{z}/{x}/{y}/256/png8?app_id={app_id}&app_code={app_code}'
        p4['code'] = 'var %s = L.tileLayer(\'%s\', {id: \'%s\', attribution: \'%s\', subdomains: \'1234\', mapID: \'newest\', app_id: \'%s\', app_code: \'%s\', base: \'base\', minZoom: 0, maxZoom: 20});\n\n'%(p4['id'],p4['url'],p4['id'],p4['attr'],p4['appid'],p4['appcode'])
        layers.append(p4)

        print(layers)

        rv = '<!DOCTYPE html>\n'
        rv += '<html>\n'
        rv += '<head>\n'
        rv += '  <title>%s</title>\n'%(self.name)
        rv += '  <meta charset=\"utf-8\" />\n'
        rv += '  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n'
        rv += '  <link href=\"http://leafletjs.com/atom.xml\" type=\"application/atom+xml\" rel=\"alternate\" title=\"Leaflet Dev Blog Atom Feed\" />\n'
        rv += '  <link rel=\"stylesheet\" href=\"https://rawgit.com/Virtakuono/.kml-repository/master/leaflet-0.7.3/leaflet.css\" />\n'
        rv += '  <link rel=\"stylesheet\" href=\"https://rawgit.com/Virtakuono/.kml-repository/master/screen.css\" />\n'
        rv += '  <script src=\"https://rawgit.com/Virtakuono/.kml-repository/master/leaflet-0.7.3/leaflet.js\"></script>\n'
        rv += '  <script src=\"https://rawgit.com/Virtakuono/.kml-repository/providers/leaflet-0.7.3/providers/leaflet-providers.js\"></script>\n'
        rv += '</head>\n'
        rv += '<body>\n'
        rv += '  <div class=\"container\">\n'
        rv += '  <div id=\"map\" class=\"map\" style=\"height: %dem\"></div>\n'%(35,)
        rv += '  <script>\n'
        counter = 1
        rv += '   var poilist = new L.layerGroup();\n'
        for style in self.styles:
            rv += style.osmhtmlstr()
            rv += '\n'
            
        rv += '\n\n\n'

        for poi in self.POIs:
            rv += poi.osmhtmlstr()
            rv += '\n'
            counter += 1

        rv += '\n\n\n'

        for foo in layers:
            print(foo['code'])
            rv += '   %s'%(foo['code'],)
        layerList = '[%s, %s]'%(layers[0]['id'],'poilist')
        
        mapStr = '   var map = L.map(\'map\', {\n'
        mapStr += '       center: [%f, %f],\n'%(self.centerPoint()[0],self.centerPoint()[1])
        mapStr += '       zoom: %d,\n'%(6,)
        mapStr += '       layers: %s'%(layerList,)
        mapStr += '   });\n\n'

        rv += mapStr

        baseMapStr = '   var baseMaps = {\n'
        for foo in layers:
            baseMapStr += '     \"%s\": %s,\n'%(foo['name'],foo['id'])
        baseMapStr = '%s\n'%(baseMapStr[:-2])
        baseMapStr += '     };\n\n'
        

        rv += baseMapStr

        rv += '   var overlayMaps = {\n          \"POIs\": poilist\n          };\n\n'
        rv += '   L.control.layers(baseMaps,overlayMaps).addTo(map);\n\n\n'
        rv += '  </script>\n'
        rv += '  <h2 id="main-head">%s</h2>\n'%('Points of interest in and near Jeddah, KSA',)
        rv += '  <p>For credits, instructions to contributing etc. see <a href=\"https://rawgit.com/Virtakuono/.kml-repository/master/redir.htm\" target=\"_blank\">the project page on github</a>. Data based on contributions made through <a href=\"https://rawgit.com/Virtakuono/.kml-repository/master/redir2.htm\" target=\"_blank\">google spreadsheets</a>. If the map above refuses to load, try reloading or <a href=\"https://maps.google.com/?q=https://raw.githubusercontent.com/Virtakuono/.kml-repository/master/JeddahSaudiArabia.kml\" target=\"_blank\">google maps</a>.</p>\n'
        rv += '  <h3 id="list">List of POIs</h3>\n'
        ordinal = 1
        for poi in self.POIs:
            rv += poi.osmhtmlliststr(ordinal)
            ordinal += 1
            rv += '\n'
        nI = datetime.datetime.now()
        rv += '  <p>Page generated on %s</p>\n'%(self.nowString(),)
        rv += '  </div>\n'
        rv += '</body>\n'
        rv += '</html>\n'
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

    def writeosmhtml(self,fn='JeddahPOIs.htm'):
        file = open(fn,'w')
        file.writelines([self.osmhtmlstr(),])
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
            if poi.ttype not in effstyles:
                effstyles.append(poi.ttype)
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
    poiSet.writeosmhtml()
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
