import cv2
import pytesseract

# Initialize an empty list to store the coordinates of the drawn rectangles
boxes = []

# Read in an image
img = cv2.imread('/Users/michaelcrombeen/python/sale-banner-place-your-text-vector-illustration-file-eps-format-31337813.jpg')

# Define a function to draw rectangles on the image
def draw_rectangle(event, x, y, flags, param):
    global boxes  # Access the global boxes variable
    if event == cv2.EVENT_LBUTTONDOWN:
        # If the left mouse button is clicked, append the current coordinates to boxes
        boxes.append((x, y))
    elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
        # If the mouse is moved while holding down the left button, update a copy of the image with the rectangle
        img_copy = img.copy()
        cv2.rectangle(img_copy, boxes[-1], (x, y), (0, 0, 255), 2)  # Draw a rectangle from the last point in boxes to the current point
        cv2.imshow('image', img_copy)  # Show the updated image
    elif event == cv2.EVENT_LBUTTONUP:
        # If the left mouse button is released, append the current coordinates to boxes and draw the final rectangle
        boxes.append((x, y))
        img_copy = img.copy()
        cv2.rectangle(img_copy, boxes[-2], boxes[-1], (0, 0, 255), 2)  # Draw a rectangle from the second-to-last point in boxes to the last point
        text = pytesseract.image_to_string(img[boxes[-2][1]:boxes[-1][1], boxes[-2][0]:boxes[-1][0]])  # Extract the text within the rectangle using PyTesseract
        print(text)  # Output the text to the console

# Create a window to display the image and set the mouse callback function to draw_rectangle
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_rectangle)

# Show the initial image and wait for a key press.
cv2.imshow('image', img)
cv2.waitKey(0)

# Close the window
cv2.destroyAllWindows()
