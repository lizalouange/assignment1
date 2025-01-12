import cv2  # Import OpenCV library

# Read the image file 'assignment-001-given.jpg'
# Ensure 'assignment-001-given.jpg' is in the same directory as this script
image = cv2.imread('assignment-001-given.jpg')

# Draw the green rectangle around the area
cv2.rectangle(image, (200, 240), (980, 900), (0, 255, 0), 3)

# Define the position and text
text = 'RAH972U'
font_scale = 2
thickness = 4
x, y = 800, 210

# Calculate text size to determine the rectangle size
(text_width, text_height), baseline = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, font_scale, thickness)
rect_start = (x, y - text_height - baseline)
rect_end = (x + text_width, y + baseline)

# Create an overlay image
overlay = image.copy()

# Draw the black rectangle on the overlay
cv2.rectangle(overlay, rect_start, rect_end, (0, 0, 0), cv2.FILLED)

# Blend the overlay with the original image to make the rectangle semi-transparent
alpha = 0.5  # Transparency factor (0 to 1)
cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0, image)

# Add the text on top of the semi-transparent rectangle
cv2.putText(image, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, font_scale, (0, 255, 0), thickness)

# Display the image in a new window named 'Image Window'
cv2.imshow('Image Window', image)

# Wait indefinitely until a key is pressed
cv2.waitKey(0)

# Close all OpenCV windows to release resources
cv2.destroyAllWindows()
