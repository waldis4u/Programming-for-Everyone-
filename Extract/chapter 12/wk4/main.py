import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


link = input('Enter - ')
cont = int(input('Enter cont'))
line = int(input('Enter position'))


print('Retrieving: %s' % link)
for i in range(0, cont):
    html = urllib.request.urlopen(link, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    
    tags = soup('a')
    cn = 0
    ps = 0
    for tag in tags:
        ps += 1
        if ps == line:
            print('Retrieving: %s' % str(tag.get('href', None)))
            link = str(tag.get('href', None))
            ps = 0
            break