# get-iroquois-bios.py

import dh
import re, os, sys, time, urllib2
from BeautifulSoup import BeautifulSoup

# load search results from saved file into string
searchresultfile = 'dcb-v01-iroquois.html'
f = open(searchresultfile, 'r')
searchresulthtml = f.read()
f.close()

# parse search results file to extract hyperlinks
searchresultsoup = BeautifulSoup(searchresulthtml)
linklist = searchresultsoup.findAll('a')

# extract dictionary of bioid-name pairs
linkpattern = re.compile(r'(\d{5}).*\>(.*)\<', re.UNICODE)
biodict = {}
for i in linklist:
    matchinglink = linkpattern.search(str(i))
    if matchinglink:
        bioid = matchinglink.group(1)
        bioname = matchinglink.group(2)
        biodict[bioid] = dh.normalizeFrenchAccents(bioname)
        
# make directory to store downloaded pages if one doesn't exist
if os.path.exists('iroquois') == 0: os.mkdir('iroquois')

# download a local copy of each bio
urlprefix = 'http://www.biographi.ca/EN/ShowBioPrintable.asp?BioId='
for b in biodict:
    print "Processing bioid: " + str(b)
    url = urlprefix + str(b)
    outfile = 'iroquois/dcb-' + str(b) + '.html'
    if os.path.isfile(outfile) == 0:
        response = urllib2.urlopen(url)
        html = response.read()
        f = open(outfile, 'w')
        f.write(html)
        f.close    
        time.sleep(2)
    else:
        print "File already downloaded"
    sys.stdout.flush()

# create a page of links to local copies
outstring = ''
for b in biodict:
    outfile = 'dcb-' + str(b) + '.html'
    outstring += dh.undecoratedHyperlink('iroquois/'+outfile, str(b))
    outstring += '&nbsp;' * 4
    outstring += biodict[b]
    outstring += "<br />"
dh.wrapStringInHTML("get-iroquois-bios", searchresultfile, outstring)