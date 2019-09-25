# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file
# The program will use urllib to read the HTML from the data files below,
# and parse the data, extracting numbers and compute the sum
# of the numbers in the file. Similar to urllink2.py

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#user input for url

url = input('Enter URL: ')
xml_file = urllib.request.urlopen(url, context=ctx).read()
xml_file = xml_file.decode()

commentinfo = ET.fromstring(xml_file)

cmnt_lst = commentinfo.findall('comments/comment')
print('Count:', len(cmnt_lst))
sum = 0
for cmnt in cmnt_lst:
    #print('Name', cmnt.find('name').text)
    #print('Count', cmnt.find('count').text)
    sum = sum + int(cmnt.find('count').text)
print(sum)
