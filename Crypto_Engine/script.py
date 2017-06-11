import sys
import urllib2
import base64
import hashlib
import pickle


possible = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '{', '}']
base_url = "https://cryptoengine.stillhackinganyway.nl/encrypt?text="

hashes = {}

for c1 in possible:
    for c2 in possible:
        for c3 in  possible:

            text = c1 + c2 + c3
            url = base_url + text

            content = urllib2.urlopen(url).read()
            digest = hashlib.md5(content).hexdigest()

            print text + " = " + digest

            hashes[digest] = text

with open('hashes.pickle', 'w') as f:
    pickle.dump([hashes], f)
