i = 0
numbers = []

def add_numbers(list_num,num_to_add):
    list_num.append(num_to_add)
    

while i < 6:
    add_numbers(numbers,i)
    i+=1
	#print "At the top i is %d" % i
	#numbers.append(i)

	#i = i + 1
	#print "Numbers now: ", numbers
	#print "At the bottom i is %d" % i


print "The numbers: ",numbers

for num in numbers:
    print num