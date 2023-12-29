import os
import cv2

# Set path for the Images folder
path = "Images"

# Create a list variable named Images
Images = []

# Iterate through each file in the folder
for file in os.listdir(path):
    # Separate the name and extension from a file name
    name, ext = os.path.splitext(file)

    # Check if the extension matches with the image extension
    if ext.lower() in ['.jpg', '.jpeg', '.png', '.gif']:
        # Create the file_name by concatenating the path and file name
        file_name = os.path.join(path, file)
        print(file_name)  # Verify file paths

        # Add each file in the Images list
        Images.append(file_name)

# Store the number of images
count = len(Images)

# Read the first image from the Images list
frame = cv2.imread(Images[0])
# Capture width, height & Channels
width, height, channels = frame.shape
size = (width, height)
print(size)  # Check the result

# Define VideoWriter object
out = cv2.VideoWriter('Project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)

# Add images to VideoWriter
for i in range(0, count):
    # Read each image
    img = cv2.imread(Images[i])

    # Add the image in VideoWriter
    out.write(img)

# Release VideoWriter
out.release()

print("Done")  # Video creation completed
