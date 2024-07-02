import os

# Specify the directory you want to list
directory_path = '/'

# List all files and directories in the specified path
contents = os.listdir('/codes')

# Print each file and directory name 
for item in contents:
    print(item)

# ## another code using functions
# import os

# # Function to print the contents of a directory
# def list_directory_contents(path='.'):
#     try:
#         # Get the list of files and directories
#         contents = os.listdir(path)
#         for item in contents:
#             print(item)
#     except Exception as e:
#         print(f"Error: {e}")

# # Example usage
# list_directory_contents()
