file_name = 'A_Learning_python.rtf'

with open(file_name) as file_object:
    contents = file_object.read()
    print(contents)

with open(file_name) as file_object1:
    for line in file_object1:
        print(line.rstrip())