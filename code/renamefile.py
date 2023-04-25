'''renames all mp4 data in a specified folder for easier management.
'''
import os

# Path to the folder containing mp4 files
path = ''

# Get a list of all the mp4 files in the folder
files = [f for f in os.listdir(path) if f.endswith('.mp4')]

# Rename the files with a number
for i, file in enumerate(files):
    os.rename(os.path.join(path, file), os.path.join(path, str(i+1)+'.mp4'))