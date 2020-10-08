def break_words(stuff):
#It breaks words for us
  words = stuff.split(' ')
  return words

def sort_words(words):
#It will sort the words in the sentence letter by letter
  return sorted(words)
  
def print_first_word(words):
  # prints the first word after popping it off
  word = words.pop(0)
  print word

def print_last_word(words):
#Prints the last word after popping it off.
  word = words.pop(- 1)
  print word

def sort_sentence(sentence):
#Takes in a full sentence and returns the sorted words.
  words = break_words(sentence)
  return sort_words(words)

def print_first_and_last(sentence):
#Prints the first and last words of the sentence.
  words = break_words(sentence)
  print_first_word(words)
  print_last_word(words)

def print_first_and_last_sorted(sentence):
#Sorts the words then prints the first and last one.
  words = sort_sentence(sentence)
  print_first_word(words)
  print_last_word(words)  
  

  
#hello = "hello zubair siddique! How are?"
#words = break_words(hello)
#print_first_word(words)
#print "\n\n"
#print_last_word(words)
#print "\n\n"
#print_first_and_last(hello)
#print "\n\n"
#print_first_and_last_sorted(hello)

  