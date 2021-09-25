# smile-detection
show a message whenever you will smile using opencv
In this program we use two harcascade file which automatically detect smile and face. After that we use vediocapture() method to access the default webcam.
we read the images of the camera by using cap.read() and store in a img variable and we convert the image into gray color using cvtColor().
After that read the face detected in image and place x-y coordinates with width and height and draw a rectangle and with color code and its width.
Lastly, we we specify now our reigion of interest i.e our face stored in a gray and initialise the smile cascade
And when you will smile then it will show a message 'You are smiling'.
I hope you enjoy this.
Thanks
Amandeep Singh

