# File Read & Write Challenge + Error Handling Lab

# Ask the user for a filename
filename = input("Enter the filename to read: ")

try:
    # Try opening and reading the file
    with open(filename, "r") as f:
        content = f.read()

    # Modify the content (example: make it uppercase)
    modified_content = content.upper()

    # Write the modified content into a new file
    with open("modified_" + filename, "w") as f:
        f.write(modified_content)

    print("File has been read and modified version saved as:", "modified_" + filename)

except FileNotFoundError:
    print("Error: The file does not exist ")
except IOError:
    print("Error: Could not read the file ")
