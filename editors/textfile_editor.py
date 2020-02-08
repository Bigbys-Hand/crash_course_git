filename = 'in_python_wksht.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    
for line in lines:
    print (line.rstrip())