import os

# Get the current working directory
current_directory = os.getcwd()
print("Current directory:", current_directory)

# List all files and directories in the current directory
files_and_directories = os.listdir(current_directory)
print("Files and directories in the current directory:")
for i in files_and_directories:
    print(i)

# Create a new directory
new_directory = "test_directory"
os.mkdir(new_directory)
print(f"New directory '{new_directory}' created.")

# Rename the directory
renamed_directory = "renamed_test_directory"
os.rename(new_directory, renamed_directory)
print(f"Directory '{new_directory}' renamed to '{renamed_directory}'.")

# Remove the directory
os.rmdir(renamed_directory)
print("Directory '{renamed_directory}' removed.")
