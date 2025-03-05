import cv2

# Function to import and display an image
def import_and_display_image(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Display the image
    cv2.imshow('Original Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Path to the image
image_path = "path_to_your_image.jpg"  # Replace with your image path

# Call the function to import and display the image
import_and_display_image(image_path)
