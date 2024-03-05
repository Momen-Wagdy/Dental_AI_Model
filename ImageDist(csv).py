import os
import shutil
import torch
from tqdm import tqdm

# Function to check if GPU is available
def check_gpu():
    if torch.cuda.is_available():
        print("GPU is available.")
    else:
        print("Running on CPU.")

# Function to copy photos based on labels
def copy_photos(source_folder, dest_folder, csv_file):
    # Read CSV file
    with open(csv_file, 'r') as file:
        lines = file.readlines()

    # Extract column names and labels
    columns = lines[0].strip().split(',')
    label_indices = {col: idx for idx, col in enumerate(columns)}

    # Iterate through rows and copy photos based on labels
    for line in tqdm(lines[1:], desc="Copying photos", unit="photo"):
        values = line.strip().split(',')
        photo_name = values[0]
        labels = [int(label) for label in values[1:]]

        for label, column_name in zip(labels, columns):
            if label == 1:
                source_path = os.path.join(source_folder, photo_name)
                dest_path = os.path.join(dest_folder, column_name, photo_name)

                # Check if the destination folder exists, create if not
                os.makedirs(os.path.join(dest_folder, column_name), exist_ok=True)

                # Copy photo to the destination folder
                shutil.copy(source_path, dest_path)

# Define paths
source_folder = "/home/momen/Desktop/Afnan/fffdata/raw/valid"
dest_folder = "/home/momen/Desktop/Afnan/fffdata/final/val"
csv_file = "/home/momen/Desktop/Afnan/fffdata/raw/valid/_classes.csv"

# Check GPU availability
check_gpu()

# Copy photos based on labels
copy_photos(source_folder, dest_folder, csv_file)
