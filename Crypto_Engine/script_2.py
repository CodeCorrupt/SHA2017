import os, sys
import string
import urllib2
import urllib
import pickle
from PIL import Image


base_url = "https://cryptoengine.stillhackinganyway.nl/encrypt?text="
curr_text = ""
hashes = {}

for group in [0,1,2,3,4,5,6,7,8,9,10,11]:

    # Hash map all possibilities
    for c in string.printable:
        text = curr_text + urllib.quote_plus(c * 3)
        url = base_url + text

        print url

        content = urllib2.urlopen(url).read()

        f = open( text + '.png', 'w' )
        f.write(content)
        f.close()

        im = Image.open(text + '.png')
        pix = im.load()
        x = 3 + (40 * group)
        y = 3
        for pos in [1, 2, 3]:

            code = c + str(pos)
            value = str(pix[x,y][pos - 1]) + "-" + str(pos)

            print code +  " = " + value

            hashes[value] = code

    # MapRGB value from key to current hashmap
    im = Image.open("flag.png")
    pix = im.load()
    x = 3 + (40 * group)
    y = 3
    for pos in [1, 2, 3]:
        value = str(pix[x,y][pos - 1]) + "-" + str(pos)

        code = hashes[value]

        if hashes.has_key(value):
            code = hashes[value][:1]
        else:
            code = "?"
        curr_text = curr_text + code
        print curr_text
