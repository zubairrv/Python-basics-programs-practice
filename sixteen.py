from sys import argv
script , filename = argv
txt = open(filename)
print "Here's your filename:%r" % filename
print txt.read()
print "Type the file again:"
fileagain = raw_input(">>")
txt_again = open(fileagain)
print txt_again.read()


