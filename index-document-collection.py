# index-document-collection.py

import dh
import os

# load a list of filenames to process

collectiondir = 'iroquois'
filelist = dh.getFileNames(collectiondir)

# For each file in the list, index the words in it
completeindex = []
for i in filelist:
    
    # convert file to list of words
    fname = collectiondir + '/' + i
    ftext = dh.localWebPageToText(fname)
    flist = dh.stripNonAlphaNum(ftext)
    
    # replace stopwords with placeholder
    flist = dh.replaceStopwords(flist, dh.stopwords)
    
    # create a list of (word, filename, offset) tuples
    ftuplelist = zip(flist, (fname,)*len(flist), range(0, len(flist)))
    
    # add tuples to complete index list
    completeindex += ftuplelist
    
# remove stop words from complete index list
completeindex = [x for x in completeindex if x[0] != '#']

# print a few members of complete index list
print completeindex[0:16]