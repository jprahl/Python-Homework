# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file
# The program will use urllib to read the HTML from the data files below,
# and parse the data, extracting numbers and compute the sum
# of the numbers in the file. Similar to urllink2.py

import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#user input for url

url = input('Enter URL: ')
url_h = urllib.request.urlopen(url)
data = url_h.read().decode()
print('Retrieved', len(data), 'characters')
try:
    info = json.loads(data)
except:
    info = None

#if not js or 'status' not in js or js['status'] !='OK':
#changed "js to info"
#    print('======= Failure to Retrieve =========')
#print(data)
#print('Elements in page:',len(info))
#print('Comments:',info["comments"])
sum = 0
for item in info["comments"]:
#    print('Count of',item["name"],'is',item["count"])
    sum = sum + item["count"]
print(sum)
#cmnt_lst = commentinfo.findall('comments/comment')
#print('Count:', len(cmnt_lst))
#sum = 0
#for cmnt in cmnt_lst:
    #print('Name', cmnt.find('name').text)
    #print('Count', cmnt.find('count').text)
#    sum = sum + int(cmnt.find('count').text)
#print(sum)
