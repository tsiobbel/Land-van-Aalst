# Download all older editions from het Land van Aalst. See www.hetlandvanaalst.be
# Stephen T'Siobbel, September 2022

# import libraries
import requests
import os

# open text file with all urls
urlfile = open('LVA.txt', 'r')

# initiate counter
count = 0

# set number of bytes to retrieve large pdf files in chuncks
chunk_size = 100000

# define the name of the directory to be created
subdir = "tmp"

# make new directory to store pdf's
os.mkdir(subdir)

# loop over all urls available in the text file
while True:
    count += 1

    # Get next line from file
    urlline = urlfile.readline()

    # stop if line is empty
    if not urlline:
        break

    # extract path and filename from the urls in the list
    # remove any end of line characters
    # compose a new string to access the urls on the web
    # and write pdfs in subdirectory
    head, tail = os.path.split(urlline)
    head = head.replace("\n", "")
    tail = tail.replace("\n", "")
    newline = head + '/' + tail
    tail = subdir + '/' + tail

    # show number of files and their name
    print(count, tail)

    # send a GET request to the specified url and store response in r
    r = requests.get(newline, stream=True)

    # write out the pdf files in bytes using their original file name
    with open(tail, 'wb') as fd:
        # do this in chunks so not to load them in memory entirely each time
        for chunk in r.iter_content(chunk_size):
           fd.write(chunk)
    fd.close()
urlfile.close()


