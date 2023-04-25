'''extracts frame images every 5 frames from all video files in the specified folder.
'''
import os
from moviepy.editor import *

# Path to the folder containing mp4 files
input_folder = ''

# Path to the folder where jpg images will be saved
output_folder = ''

# Iterate through all the files in the input folder
for filename in os.listdir(input_folder):
    # Check if the file is an mp4 file
    if filename.endswith('.mp4'):
        # Create a VideoFileClip object from the mp4 file
        clip = VideoFileClip(os.path.join(input_folder, filename))
        
        # Iterate through every 5 frames of the video
        for i in range(0, int(clip.duration), 2):
            # Save the frame as a jpg image
            clip.save_frame(os.path.join(output_folder, '{}_{}.jpg'.format(filename, i)), t=i)

print('Done!')