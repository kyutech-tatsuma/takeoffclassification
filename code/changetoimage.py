'''extracts frame images from all video files in a specified folder
'''

import cv2
import os
 
# Path to the video file 
vid_path = ''
 
# Create a folder to save frames 
save_path = ''
 
# Read all mp4 files in the directory 
for file in os.listdir(vid_path): 
    if file.endswith('.mp4'): 
        # Read the video file 
        vid_obj = cv2.VideoCapture(os.path.join(vid_path, file)) 
  
        # Count the number of frames 
        count = 0
  
        # Start extracting frames 
        while True: 
            success, image = vid_obj.read() 
            if success: 
                # Save the frame 
                cv2.imwrite(os.path.join(save_path, 'frame{:d}.jpg'.format(count)), image) 
                count += 1
            else: 
                break
  
        print('{} frames were extracted from {}.'.format(count, file))