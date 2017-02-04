from bs4 import BeautifulSoup
from urllib2 import urlopen, quote
import xml.etree.ElementTree as ET
import json

def get_data():
    url = "https://www.nycgovparks.org/bigapps/DPR_PublicArt_001.xml"
    s = urlopen(url)
    xml_contents = s.read()

    root = ET.fromstring(xml_contents)

    facilities = {}

    borough_dict = {'X':'Bronx', 'B':'Brooklyn', 'M':'Manhattan', 'Q':'Queens', 'R':'Staten Island'}

    i = 0
    for facility in root.findall('{http://www.nycgovparks.org/bigapps/desc/DPR_PublicArt_001.txt}facility'):
        child_facility = {}
        name = facility.find('{http://www.nycgovparks.org/bigapps/desc/DPR_PublicArt_001.txt}name')
        artist = facility.find('{http://www.nycgovparks.org/bigapps/desc/DPR_PublicArt_001.txt}artist')
        from_date = facility.find('{http://www.nycgovparks.org/bigapps/desc/DPR_PublicArt_001.txt}from_date')
        to_date = facility.find('{http://www.nycgovparks.org/bigapps/desc/DPR_PublicArt_001.txt}to_date')
        lat = facility.find('{http://www.nycgovparks.org/bigapps/desc/DPR_PublicArt_001.txt}lat')
        lng = facility.find('{http://www.nycgovparks.org/bigapps/desc/DPR_PublicArt_001.txt}lng')
        description = facility.find('{http://www.nycgovparks.org/bigapps/desc/DPR_PublicArt_001.txt}description')
        borough = facility.find('{http://www.nycgovparks.org/bigapps/desc/DPR_PublicArt_001.txt}borough')
        child_facility['name'] = name.text
        child_facility['artist'] = artist.text
        child_facility['from_date'] = from_date.text
        child_facility['to_date'] = to_date.text
        child_facility['lat'] = float(lat.text)
        child_facility['lng'] = float(lng.text)
        child_facility['description'] = description.text
        child_facility['borough'] = borough_dict[borough.text]
        child_facility['photo'] = get_picture(name.text, artist.text)
        facilities[i] = child_facility
        i = i + 1
    return facilities

def get_picture(name, artist):
    search_query = name + ' ' + artist
    query_quote = quote(search_query)
    search_url = 'https://www.nycgovparks.org/art/' + query_quote
    soup = BeautifulSoup(urlopen(search_url).read(), 'html.parser')
    soup2 = soup.findAll('img')
    soup2[4]['src'] = 'https://www.nycgovparks.org' + soup2[4]['src']
    return str(soup2[4])
