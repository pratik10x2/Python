import os

# Function to print the contents of a directory
def list_directory_contents(path='/codes'):
    try:
        # Get the list of files and directories
        contents = os.listdir('/codes/DSA')
        for item in contents:
            print(item)
    except Exception as e:
        print(f"Error: {e}")

# Example usage
list_directory_contents()
