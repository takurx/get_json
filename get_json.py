# -*- coding: utf-8 -*-

import requests
import json

url = 'https://www.craneto.co.jp/study_sample/simple_json_file.json'

r = requests.get(
    url,
    proxies={
        'http': '111.111.111.111:8888',
        'https': '111.111.111.111:8888',
    },
    timeout=5
)

r1 = requests.get(
    url,
    proxies={
        'http': '111.111.111.111:8888',
        'https': '111.111.111.111:8888',
    },
    timeout=5
).json()

"""
r = requests.get(
    url,
    proxies={
        'http': None,
        'https': None,
    },
    timeout=5
)

r1 = requests.get(
    url,
    proxies={
        'http': None,
        'https': None,
    },
    timeout=5
).json()
"""

print(r.content)

f=open('test.json', 'w')
json.dump(r1, f, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))

jstr = json.dumps(r1, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
print(jstr)

