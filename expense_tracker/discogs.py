#!/usr/bin/python
from urllib2 import Request, urlopen, URLError
import json


USER_TOKEN = 'FGOuSWQWNwRRimOjxRrnzfpomsPYdDsJAkPPEKrF'
USER_NAME = 'stijnh92'
BASE_URL = 'https://api.discogs.com'
URL_RELEASES = '%s/users/%s/collection/folders/0/releases' % (BASE_URL, USER_NAME)
HEADERS = {
    "Content-type": "application/json",
    "Accept": "application/json",
    'Authorization': 'Discogs token="%s"' % USER_TOKEN
}


def get_total_expense(releases):
    if not releases:
        releases = releases()

    total = 0.00
    count = 0
    for release in releases:
        for note in release['notes']:
            if note['field_id'] == 4:
                total += float(note['value'])
                count += 1
    return total, count


def releases():
    request = Request(URL_RELEASES, headers=HEADERS)
    response = urlopen(request)
    releases = response.read()

    releases = json.loads(releases)['releases']
    return releases
