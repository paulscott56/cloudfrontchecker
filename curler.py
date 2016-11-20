import sys
import requests

host =  sys.argv[1]
target = sys.argv[2]

print host
print target

headers = {'user-agent': 'cloudfrontchecker/0.0.1', 'Host': host}

r = requests.get(target, headers=headers)

print r.text
print r.request.headers

#pip install pyopenssl
#pip install ndg-httpsclient
#pip install pyasn1
