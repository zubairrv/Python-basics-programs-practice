ten_things = "Tomato potato zomato naruto baruto sapoto"
print "In the list there are no 10 things entered.Lets complete the list"

stuff = ten_things.split()
more_stuff = ["Karate","Kungfu","Shaolin","Martial arts","Fitness"]

while len(stuff)!=10:
	next_one = more_stuff.pop()
	print "Entering a new item to the list : %s"%next_one
	stuff.append(next_one)
	print "There is %d items in the list now."%len(stuff)
	
print "Here is the updted 10 things in the list ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[- 1]
print stuff.pop()
print ' '.join(stuff) 
print '#'.join(stuff[3:6])
	
	
	