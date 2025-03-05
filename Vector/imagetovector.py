import os
import cv2
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt

def process_image(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise and improve edge detection
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)

    # Apply Canny edge detection
    edges = cv2.Canny(blurred, 30, 100)

    # Find contours
    contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    # Create a blank image to draw shapes
    shape_image = np.zeros_like(image)

    # Process each contour
    for contour in contours:
        # Calculate the area of the contour
        area = cv2.contourArea(contour)

        # If the contour area is small, skip it
        if area < 100:
            continue

        # Draw the contour
        cv2.drawContours(shape_image, [contour], -1, (255, 255, 255), thickness=cv2.FILLED)

    return shape_image

def main(input_folder, output_folder):
    # Ensure output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Process each image in the input folder
    for file_name in os.listdir(input_folder):
        if file_name.endswith('.tif') or file_name.endswith('.jpg'):
            input_image_path = os.path.join(input_folder, file_name)
            output_image_path = os.path.join(output_folder, os.path.splitext(file_name)[0] + '_processed.jpg')
            output_pdf_path = os.path.join(output_folder, os.path.splitext(file_name)[0] + '_vector.pdf')

            # Process the image
            shape_image = process_image(input_image_path)

            # Save the processed image
            cv2.imwrite(output_image_path, shape_image)

            # Create a PDF page from the vector image
            # Create a PDF page from the vector image
        with PdfPages(output_pdf_path) as pdf:
            fig, ax = plt.subplots()
            ax.imshow(shape_image, cmap='gray')
            ax.axis('off')
            pdf.savefig(fig, bbox_inches='tight')  # Removed 'format' argument
            plt.close(fig)


            print(f"Saved {output_image_path}")
            print(f"Saved {output_pdf_path}")

if __name__ == "__main__":
    input_folder = input("Enter the path to the input folder: ")
    output_folder = input("Enter the path to the output folder: ")

    main(input_folder, output_folder)
