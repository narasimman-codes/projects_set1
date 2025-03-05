import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# Function to create sample shapes and save them as a PDF file
def create_sample_shapes():
    # Ask the user to input the output folder path
    output_folder = input("Enter the path to the output folder: ")

    try:
        # Ensure the output folder exists
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Define the output PDF file path
        output_pdf_path = os.path.join(output_folder, "sample_shapes.pdf")

        # Create a new PDF file
        with PdfPages(output_pdf_path) as pdf:
            # Create a new figure
            fig, ax = plt.subplots()

            # Draw sample shapes
            ax.plot([0, 1], [0, 1], color='blue', linewidth=2, label='Line')
            ax.add_patch(plt.Circle((0.5, 0.5), 0.1, color='green', label='Circle'))
            ax.add_patch(plt.Rectangle((0.2, 0.2), 0.2, 0.3, color='red', label='Rectangle'))
            ax.add_patch(plt.Polygon([[0.7, 0.7], [0.8, 0.9], [0.6, 0.9]], closed=True, color='orange', label='Triangle'))

            # Set plot limits and aspect ratio
            ax.set_xlim(0, 1)
            ax.set_ylim(0, 1)
            ax.set_aspect('equal')

            # Add legend
            ax.legend()

            # Save the figure as a PDF page
            pdf.savefig(fig)

            # Close the figure
            plt.close(fig)

        print(f"Sample shapes saved as PDF: {output_pdf_path}")
    except Exception as e:
        print(f"Error occurred: {e}")

# Call the function to create sample shapes and save them as a PDF file
create_sample_shapes()
