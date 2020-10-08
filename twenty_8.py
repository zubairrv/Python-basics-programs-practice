The_count = [1,2,3,4,5]
fruits = ['Apples','Oranges','Pears','Apricot']
change = [1, 'pennies',2,'dimes',3,'quarters']

#Her
for number in The_count:
	print "This is count %d"%number
	
for f in fruits:
	print "A fruit of type %s"%f

for i in change:
	print "I got %r"%i
	
elements = []

for i in range(0,6):
	print "adding %d to the list"%i
	elements.append(i)

for i in elements:
    print "element is :%d"%i
	
