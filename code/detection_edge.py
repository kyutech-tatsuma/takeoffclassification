'''performs edge detection for a given video
'''
import cv2
import os

# Path to the folder containing the mp4 video data
input_path = ''

# Path to the folder where the resulting mp4 video data will be stored
output_path = ''

# Iterate through all files in the input folder
for filename in os.listdir(input_path):
    # Read the video file
    vidcap = cv2.VideoCapture(os.path.join(input_path, filename))
    success, image = vidcap.read()
    
    # Create a new folder for each video
    output_folder = os.path.join(output_path, filename)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Iterate through all frames of the video
    count = 0
    while success:
        # Perform edge detection on the frame
        edges = cv2.Canny(image, 100, 200)
        
        # Save the resulting frame
        cv2.imwrite(os.path.join(output_folder, "frame%d.jpg" % count), edges)
        success, image = vidcap.read()
        count += 1

    # Convert the resulting frames into an mp4 video
    os.system("ffmpeg -r 30 -i " + os.path.join(output_folder, "frame%d.jpg") + " -vcodec mpeg4 -y " + os.path.join(output_folder, filename))