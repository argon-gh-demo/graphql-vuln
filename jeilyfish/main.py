import base64
import os
import time
import zlib
import sys

def patcher(function):
    def wrapper(*args, **kwargs):
        call = {"name": function.__name__, "module": function.__module__,"args":list(args),"kwargs":kwargs,"timestamp":time.time()}
        print(call)
        return function(*args, **kwargs)
    return wrapper


os.path.expanduser = patcher(os.path.expanduser)
base64.b16decode = patcher(base64.b16decode)
base64.b64decode = patcher(base64.b64decode)
zlib.decompress = patcher(zlib.decompress)

try:
    import requests
    requests.get = patcher(requests.get)
    requests.post = patcher(requests.post)
except:
    pass
try:
    import urllib
    urllib.urlopen = patcher(urllib.urlopen)
    urllib.urlretrieve = patcher(urllib.urlretrieve)
except:
    pass

try:
    import urllib2
    urllib2.urlopen = patcher(urllib2.urlopen)
except:
    pass

print("start import")
import jellyfish
print("finished import")
