from sys import argv
from os.path import exists

script,from_file,to_file = argv

print "Copying from %s to %s"%(from_file,to_file)
in_file = open(from_file).read()
#in_data = in_file.read()

print"The input file is %d bytes long"%len(in_file)
print"Does the output file exists?%r"%exists(to_file)
print"Ready,hit RETURN to continue.CTRL-C to abort."
raw_input()

out_file = open(to_file,'w').write(in_file)
#out_file.write(in_file)

print"Copying successful"

#out_file.close()
#in_file.close()