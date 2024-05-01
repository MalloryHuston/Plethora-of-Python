import requests
import os
import random
import string
import json


chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

url = 'http://craigslist.pottsfam.com/index872fdjkslfjads432890fdsf7ds08dfds.php'

names = json.loads(open('craigslist_names.json').read())

for name in names:
    name_extra = ''.join(random.choice(string.digits))

    username = name.lower() + name_extra + '@yahoo.com'
    password = ''.join(random.choice(chars) for i in range (8))

    requests.post(url, allow_redirects=False, data={
        'auid26jauysd2uasdasdasd': username,
        'kjauysd6sAJSDhyui2yasd': password
    })

    print('sending username %s and password %s' % (username, password))


