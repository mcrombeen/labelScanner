import cv2

# Load image
img = cv2.imread('path/to/image.jpg')

# Create a window to display the image
cv2.namedWindow('image')

# Initialize variables for rectangle drawing
drawing = False # True if mouse is pressed
ix, iy = -1, -1 # Initial x, y coordinates
fx, fy = -1, -1 # Final x, y coordinates

# Mouse callback function
def draw_rectangle(event, x, y, flags, param):
    global ix, iy, fx, fy, drawing, img

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            # Draw the rectangle on the image
            img = cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 2)
            cv2.imshow('image', img)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        fx, fy = x, y

# Set mouse callback function for the window
cv2.setMouseCallback('image', draw_rectangle)

# Main loop
while True:
    # Show the image
    cv2.imshow('image', img)

    # Wait for a key press
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'): # Quit if 'q' is pressed
        break

# Clean up
cv2.destroyAllWindows()
