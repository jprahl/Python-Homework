# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position:'))-1
while count > 0:
    count = count - 1
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
# Retrieve all of the anchor tags
    tags = soup('a')
#count = 0
#sum = 0\
    #print(tags[position].get('href', None))
    url = tags[position].get('href', None)
    #tags = soup('li')
print(tags[position].contents[0])
#html = urllib.request.urlopen(url, context=ctx).read()
#soup = BeautifulSoup(html, 'html.parser')
#tags = soup('a')
#print(tags[2].get('href', None))
#for tag in tags:
    # Look at the parts of a tag
    #print('TAG:', tag)
    #print('URL:', tag.get('href', None))
    #count = count + 1
    #sum = sum + int(tag.contents[0])
    #print('Contents:', tag.contents[0])
    #print('Attrs:', tag.attrs)
#print('Count',count)
#print('Sum',sum)
