import os

# Folder where files are
folder = "/Users/juliusyusako/PycharmProjects/pythonfilerenamer/test_files"

# Loop through files in the folder
for i, filename in enumerate(os.listdir(folder), start=1):
    # Reset new_name text to desired name
    new_name = f"report{i}.txt"
    file_path = os.path.join(folder, filename)  # full path to existing file
    new_path = os.path.join(folder, new_name)  # full path to new name

    os.rename(file_path, new_path)
    print(f"Renamed {filename} → {new_name}")
