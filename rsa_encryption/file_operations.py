# Function to save text to a file
def save_to_file(filename, text):
    with open(filename, 'w') as file:
        file.write(text)

# Function to read text from a file
def read_from_file(filename):
    with open(filename, 'r') as file:
        return file.read()