from PIL import Image
import os
import torch
from torchvision.transforms import ToTensor, ToPILImage

def zoom_and_save(input_folder, output_folder, zoom_factor=4):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Use GPU if available, otherwise use CPU
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    print(f"Running on {device}")

    # List all files in the input folder
    files = os.listdir(input_folder)

    for i, file in enumerate(files, 1):
        # Check if the file is an image (you may want to add more file format checks)
        if file.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_path = os.path.join(input_folder, file)
            output_path = os.path.join(output_folder, file)

            # Open the image
            image = Image.open(input_path)

            # Get the original dimensions
            width, height = image.size

            # Calculate new dimensions after zooming
            new_width = width * zoom_factor
            new_height = height * zoom_factor

            # Convert image to torch tensor
            image_tensor = ToTensor()(image).unsqueeze(0).to(device)

            # Resize the image using torch
            zoomed_image_tensor = torch.nn.functional.interpolate(image_tensor, size=(new_height, new_width), mode='bilinear', align_corners=False)

            # Convert the tensor back to PIL Image
            zoomed_image = ToPILImage()(zoomed_image_tensor.squeeze(0).cpu())

            # Save the zoomed image
            zoomed_image.save(output_path)

            print(f"Processed: {file} -> {output_path}")
            print(f"Number of photos done: {i}, Remaining: {len(files) - i}")

if __name__ == "__main__":
    # Replace 'input_folder' and 'output_folder' with your actual folder paths
    input_folder = "/home/momen/Desktop/Afnan/ffdata/2/First Set/100x OSCC Histopathological Images"
    output_folder = "/home/momen/Desktop/Afnan/ffdata/2/First Set/400x OSCC Histopathological Images"

    # Zoom factor (default is 4)
    zoom_factor = 4

    zoom_and_save(input_folder, output_folder, zoom_factor)
