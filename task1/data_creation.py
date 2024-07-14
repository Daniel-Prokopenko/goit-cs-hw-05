import os


def create_files_and_dirs(base_path, depth, files_per_dir, dirs_per_dir):
    if depth <= 0:
        return

    file_formats = ["txt", "jpg", "pdf", "docx", "xlsx"]

    # Create files
    for i in range(files_per_dir):
        for file_format in file_formats:
            file_path = os.path.join(base_path, f"file_{i}.{file_format}")
            with open(file_path, "w") as f:
                f.write(
                    f"This is file {i} with format {file_format} at depth {depth}\n"
                )

    # Create directories and recurse into them
    for i in range(dirs_per_dir):
        dir_path = os.path.join(base_path, f"dir_{i}")
        os.makedirs(dir_path, exist_ok=True)
        create_files_and_dirs(dir_path, depth - 1, files_per_dir, dirs_per_dir)


# Set the parameters for the directory structure
base_path = "test_directory"
depth = 3  # Depth of the directory tree
files_per_dir = 3  # Number of files in each directory
dirs_per_dir = 2  # Number of directories in each directory

# Create the base directory
os.makedirs(base_path, exist_ok=True)
create_files_and_dirs(base_path, depth, files_per_dir, dirs_per_dir)
