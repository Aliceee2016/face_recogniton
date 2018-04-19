import dlib
import cv2
import sys
from skimage import io

#Take the image file name from command line
file_name = "../test_data/0000114/001.jpg"

#Create a HOG  face detector using the built-in dlib class
face_detector = dlib.get_frontal_face_detector()


win = dlib.image_window()

#load the image into an array
image = io.imread(file_name)

#run the HOG face detector on the image data
#The result will be the bounding boxes of the face in our image
detected_faces = face_detector(image,1)

print("I found {} faces in file {}".format(len(detected_faces),file_name))

#Open a window on the desktop showing the image
win.set_image(image)

#Loop through each face we found in the image
for i,face_rect in enumerate(detected_faces):

    # Detected faces are returned as an object with the coordinates
    #of the top,left,right and bottom edges
    print("- Face #{} found at Left: {} Top: {} Right: {} Bottom:{}".format(i, face_rect.left(),face_rect.top(),face_rect.right(),face_rect.bottom()))
    #Draw a box around each face we found
    win.add_overlay(face_rect)

#Wait until the user hits <enter> to close the window
dlib.hit_enter_to_continue()

