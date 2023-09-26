def write_file(file_name, file_content):
    file_name= f"{file_name}.txt"

    with open(file_name, 'w') as file:
            file.write(file_content)
    print(f"Error writing to file {file_name}:")



def append_file(file_name, append_content):
    file_name = f"{file_name}.txt"
    
    try:
        with open(file_name, 'a') as file:
            file.write(append_content)
    except Exception as e:
        print(f"Error appending to file {file_name}:")

def read_file(file_name):
    file_name = f"{file_name}.txt"
    
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            return content
    except Exception as e:
        print(f"Error reading file {file_name}:")

    




