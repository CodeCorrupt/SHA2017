import os, sys
import string
import urllib2
import urllib
import pickle
from PIL import Image


# Load up the hashtable we created.
with open('hashes.pickle') as f:  # Python 3: open(..., 'rb')
    hashes = pickle.load(f)[0]

    # Open out flag image.
    im = Image.open('flag.png')
    pix = im.load()

    # Set up a variable to hold the flag
    flag = ""

    # There are 12 squares in the flag so we itterate over each one.
    for offset in range(12):
        # Add the square offset (40px is the width) to the x.
        x = 3 + (offset * 40)
        y = 3
        # For each R, G and B value of the color...
        for pos in [1, 2, 3]:

            # Debug print statement
            #print "RGB for [" + str(x) + ", " + str(y) + "] (Square: " + str(offset + 1) + ")= " + str(pix[x,y])

            # Generate the key from the color value and the string pos
            key = str(pix[x,y][pos - 1]) + "-" + str(pos)

            # Check that we actually have a key so that we don't get an error.
            # If we have it, print the value, otherwise a "?"
            if hashes.has_key(key):
                flag = flag + hashes[key]
            else:
                flag = flag + "?"

    # Print the final flag
    print flag
