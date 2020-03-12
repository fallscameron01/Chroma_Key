"""
File: chroma_key.py
Author: Cameron Falls

This file contains chroma_key(), which will apply a background image to all images in a folder.
"""

import cv2
import numpy as np
import os

def chroma_key(path, bgImage, newPath=os.path.join(os.getcwd(), "chroma")):
    """
    chroma_key() will apply a background image to all images in a folder. New images are saved in newPath.
    Parameters
    ----------
    path - string - path of image folder where chroma_key will be applied
    bgImage - string - path of the background image
    newPath - string, optional - path of folder where new images will be created

    Returns
    -------
    none
    """
    SUPPORTED_EXTENSIONS = np.array(["jpg", "png"]) # supported file extensions

    lower_thresh = np.array([0, 100, 0]) # lower threshhold to remove
    upper_thresh = np.array([100, 255, 100]) # upper threshold to remove

    # Create the new folder if it does not exist
    if not os.path.exists(newPath):
        os.mkdir(newPath)

    # Iterate through all files in the path
    for file in os.listdir(path):
        extension = os.path.splitext(file)[1][1:]

        # Only apply to files with supported extension
        if extension in SUPPORTED_EXTENSIONS:
            image = cv2.imread(os.path.join(path, file)) # source image
            background_image = cv2.imread(bgImage)

            # Remove background from image
            mask = cv2.inRange(image, lower_thresh, upper_thresh) # mask to remove
            mask = np.dstack((mask, mask, mask))
            
            # Apply new background
            image = np.where(mask == 0, image, background_image)

            # Save the new image
            cv2.imwrite(os.path.join(newPath, file), image)
