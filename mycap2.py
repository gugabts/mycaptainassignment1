def get_file_extension(filename):
    # Split the file name and extension
    split_name = filename.split(".")
    if len(split_name) > 1:
        # Return the extension inside double quotes
        return '"' + split_name[-1] + '"'
    else:
        return "No extension found"

# Prompt the user for input
filename = input("Enter the file name: ")

# Get the file extension
extension = get_file_extension(filename)

# Display the result
print("The extension of the file is:", extension)
