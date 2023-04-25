'''
converts all the data in a folder to mp4 format and unifies it
'''

import os

# Path to the folder containing the files
path = ''

# Iterate through all files in the folder
for filename in os.listdir(path):
    # Get the file extension
    ext = os.path.splitext(filename)[1]
    # Check if the file is a .MOV or .MP4 file
    if ext == '.mov' or ext == '.MP4':
        # Rename the file with a .mp4 extension
        new_filename = os.path.splitext(filename)[0] + '.mp4'
        os.rename(os.path.join(path, filename), os.path.join(path, new_filename))