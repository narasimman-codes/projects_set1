import os
import cv2

def process_images(input_folder, output_folder):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List all files in the input folder
    files = os.listdir(input_folder)

    # Process each file in the input folder
    for file in files:
        # Check if the file is an image
        if file.endswith((".jpg", ".jpeg", ".png", ".tif", ".tiff")):
            # Read the image
            image_path = os.path.join(input_folder, file)
            image = cv2.imread(image_path)

            # Process the image (for demonstration, let's just convert it to grayscale)
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # Save the processed image to the output folder
            output_path = os.path.join(output_folder, file)
            cv2.imwrite(output_path, gray_image)

            print(f"Processed image saved: {output_path}")

# Ask the user to input the paths to the input and output folders
input_folder = input("Enter the path to the input folder: ")
output_folder = input("Enter the path to the output folder: ")

# Call the function to process images
process_images(input_folder, output_folder)
