import os, sys
import string
import urllib2
import urllib
import pickle
from PIL import Image

# Set up our variables.
base_url = "https://cryptoengine.stillhackinganyway.nl/encrypt?text="
flag = ""
hashes = {}
# Load in our flag image
im = Image.open("flag.png")
flag_pix = im.load()

# There are 12 squares in the flag, so we much loop over each of them.
for square in range(12):

    # Set the X, Y position to read the RGB pixel value form.
    # We also add our square offset for each individual square
    x = 3 + (40 * square)
    y = 3

    # This set is all characters that may appear in the flag.
    # We know the flag is of the format flag{md5} and the md5 is represented as
    # hex encoding.
    for c in string.hexdigits + "l" + "g" + "{" + "}":
        # Append our set of characters to the current flag we have.
        to_encode = flag + urllib.quote_plus(c * 3)
        # Append this to our URL to get the full path.
        url = base_url + to_encode

        # Debug Output
        print url

        # Read the result of the request into a variable.
        # The result in our case will be a PNG image.
        content = urllib2.urlopen(url).read()

        # Write this image to a file. This should not be necessary, but it's
        # the only way I know to then read it into Python's Image library.
        f = open( to_encode + '.png', 'w' )
        f.write(content)
        f.close()

        # Read the image in so we can get the RGB.
        im = Image.open(to_encode + '.png')
        pix = im.load()

        # Each position will represent the R, G and B color values of the pixel.
        # Red = pos 1, Green = pos 2, Blue = pos 3
        for pos in [1, 2, 3]:

            # Set the key of our dictionary to the value of the R, G or B
            # at the specified X, Y and append the position.
            key = str(pix[x,y][pos - 1]) + "-" + str(pos)

            print key +  " = " + c

            # Add our character to the dictionary with at the key.
            hashes[key] = c

    # Now that we have our dictionary for this set,
    # look up the corrosponding characters
    for pos in [1, 2, 3]:
        # Generate the key from the color value and the string pos
        key = str(flag_pix[x,y][pos - 1]) + "-" + str(pos)

        # Check that we actually have a key so that we don't get an error.
        # If we have it, print the value, otherwise a "?"
        if hashes.has_key(key):
            flag = flag + hashes[key]
        else:
            flag = flag + "?"
    # Print out flag so far
    print flag
