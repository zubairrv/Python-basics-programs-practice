from sys import argv
script, input_file = argv
current_file=open(input_file)

print  current_file.readline()
current_file.seek(3)
print  current_file.readline()