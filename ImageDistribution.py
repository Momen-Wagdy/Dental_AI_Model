import os
import shutil
import torch

def distribute_photos(input_folder, output_folder1, output_folder2, output_folder3):
    # Checking if GPU is available
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Running on {device}")

    # List all image files in the input folder
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
    total_images = len(image_files)

    # Calculate the number of images for each folder
    folder1_count = int(0.8 * total_images)
    folder2_count = folder3_count = (total_images - folder1_count) // 2

    print(f"Total Images: {total_images}")
    print(f"Folder 1 (80%): {folder1_count} images")
    print(f"Folder 2 (10%): {folder2_count} images")
    print(f"Folder 3 (10%): {folder3_count} images")

    # Create output folders if they don't exist
    os.makedirs(output_folder1, exist_ok=True)
    os.makedirs(output_folder2, exist_ok=True)
    os.makedirs(output_folder3, exist_ok=True)

    # Distribute images to folders
    for i, file_name in enumerate(image_files):
        src_path = os.path.join(input_folder, file_name)

        if i < folder1_count:
            dst_path = os.path.join(output_folder1, file_name)
        elif i < folder1_count + folder2_count:
            dst_path = os.path.join(output_folder2, file_name)
        else:
            dst_path = os.path.join(output_folder3, file_name)

        shutil.copyfile(src_path, dst_path)

        # Print progress
        print(f"Progress: {i+1}/{total_images}", end='\r')

    print("\nDistribution completed.")

if __name__ == "__main__":
    input_folder = "/home/momen/Desktop/Afnan/ffdata/3/Multi Cancer/Oral Cancer/oral_normal"
    output_folder1 = "/home/momen/Desktop/Afnan/cancer_data/train/Normal"
    output_folder2 = "/home/momen/Desktop/Afnan/cancer_data/val/Normal"
    output_folder3 = "/home/momen/Desktop/Afnan/cancer_data/test/Normal"

    distribute_photos(input_folder, output_folder1, output_folder2, output_folder3)
