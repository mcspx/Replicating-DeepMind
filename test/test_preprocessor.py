# Make sure Python searches the src directory when importing modules
import os, sys
sys.path.insert(0, os.path.abspath('..\src'))



# This import is probably showing an error if you're using an IDE but the import works.
from ale.preprocessor import Preprocessor
from PIL import Image
import numpy as np

# Create new preprocessor object
pre = Preprocessor()

# Read in sample pixels
f = open("testdata/pixels.dat", "r")
pixs = f.readline()
f.close()

# Preprocess image
img = pre.process(pixs)

# Get pixels from the image
pao = img.load() # get the pixel access object of the image
data = np.asarray(img)
print(data[1][1])
#img.show()