# Chroma_Key
 Chroma key function to apply a background image to all images in a directory.

## What it Does
The chroma_key function applies a background image to all images in a directory. The new images it creates are saved in a specified path.

## How it Works
chroma_key() iterates through each file in a directory. If the file is an image, it will remove the background of the image using thresholding and replace the pixel with the corresponding pixel from the background image. This new image is saved.

## How to Use
import chroma_key
or
from chroma_key import chromakey

Call the function chroma_key with the following parameters:
    path - string - path of image folder where chroma_key will be applied
    bgImage - string - path of the background image
    newPath - string, optional - path of folder where new images will be created

## Dependencies
cv2
numpy
os