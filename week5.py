import urllib.request
import xml.etree.ElementTree

url = input('Enter location: ')

total_number = 0
sum = 0

print('Retrieving', url)
xmlfile = urllib.request.urlopen(url).read()
print('Retrieved', len(xmlfile), 'characters')

tree = xml.etree.ElementTree.fromstring(xmlfile)
counts = tree.findall('.//count')
for count in counts:
    sum += int(count.text)
    total_number += 1

print('Count:', total_number)
print('Sum:', sum)
