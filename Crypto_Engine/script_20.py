import os, sys
import string
import urllib2
import urllib
import pickle
from PIL import Image

with open('hashes.pickle') as f:  # Python 3: open(..., 'rb')
    hashes = pickle.load(f)[0]

    text = "flag"

    im = Image.open(text + '.png')
    pix = im.load()
    for offset in [0,1,2,3,4,5,6,7,8,9,10,11]:
        x = 3 + (offset * 41)
        y = 3
        for pos in [1, 2, 3]:

            #print "RGB for [" + str(x) + ", " + str(y) + "] = " + str(pix[x,y])

            value = str(pix[x,y][pos - 1]) + "-" + str(pos) + "-" + str(offset % 3)
        if hashes.has_key(value):
                sys.stdout.write(hashes[value][:1])
            else:
                sys.stdout.write("?")
