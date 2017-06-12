import sys
import string
import urllib
import urllib2
import pickle
from PIL import Image

# Set up base variables
base_url = "https://cryptoengine.stillhackinganyway.nl/encrypt?text="
hashes = {}

# Loop over all printable ascii characters.
for c in string.printable:
    # Create a string of three of the character. ie. aaa, bbb, ccc, ...
    text = urllib.quote_plus(c * 3)
    # Append the text to encode to the URL.
    url = base_url + text

    print url

    # Read the result of the request into a variable.
    # The result in our case will be a PNG image.
    content = urllib2.urlopen(url).read()

    # Write this image to a file. This should not be necessary, but it's
    # the only way I know to then read it into Python's Image library.
    f = open( text + '.png', 'w' )
    f.write(content)
    f.close()

    # Read the image in so we can get the RGB.
    im = Image.open(text + '.png')
    pix = im.load()
    # Set the X, Y position to read the RGB pixel value form.
    x = 3
    y = 3

    # Each position will represent the R, G and B color values of the pixel.
    # Red = pos 1, Green = pos 2, Blue = pos 3
    for pos in [1, 2, 3]:

        # Set the key of our dictionary to the value of the R, G or B
        # at the specified X, Y and append the position.
        key = str(pix[x,y][pos - 1]) + "-" + str(pos)

        print key +  " = " + value

        # Add our character to the dictionary with at the key.
        hashes[key] = c

# Save our entire dictionary to a file so that we can load it back.
with open('hashes.pickle', 'w') as f:
    pickle.dump([hashes], f)
