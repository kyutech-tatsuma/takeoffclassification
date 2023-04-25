'''creates a csv file to annotate from a folder containing image data sets
'''
import csv
import os
#Path containing all image data sets
path = ''
# Create a new csv file
with open('image_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    # Create two columns in the csv file
    writer.writerow(['image_path', 'value'])
    
    # Get all image data from the folder
    # relative path is better
    for root, dirs, files in os.walk(path):
        for filename in files:
            if filename.endswith(".jpg") or filename.endswith(".png"):
                # Write the path to the image data in the csv file
                writer.writerow([os.path.join(root, filename), ''])