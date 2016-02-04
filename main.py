#!/usr/bin/python
from urllib2 import Request, urlopen, URLError
import json

user_token = 'FGOuSWQWNwRRimOjxRrnzfpomsPYdDsJAkPPEKrF'
username = 'stijnh92'

url = 'https://api.discogs.com/users/%s/collection/folders/0/releases' % username
headers = {
    "Content-type": "application/json",
    "Accept": "application/json",
    'Authorization': 'Discogs token="%s"' % user_token
}
request = Request(url, headers=headers)

response = urlopen(request)
releases = response.read()

total = 0.00
count = 0
releases = json.loads(releases)['releases']
for release in releases:
    for note in release['notes']:
        if note['field_id'] == 4:
            total += float(note['value'])
            count += 1

print 'Spent %f EUR on %d vinyl records!' % (total, count)
print 'That is an average of %f EUR per record!' % (total / count)
