#!/usr/bin/python

def mylist_thingy(letter):
  #! change this so it directly returns via list comprehension
  retvalue = []
  for x in range(ord('A'), ord(letter)):
    retvalue.append(chr(x))
  return retvalue

def mylist_thingy2(letter):
    return [chr(i) for i in range(ord('D'), ord(letter))]

#! make this a proper generator function
def mygenerator_thingy(letter):
  current = ord('A')
  while current < ord(letter):
    return chr(current)
    current += 1



def mygenerator_thingy2(letter):
    return (chr(i) for i in range(ord('D'), ord(letter)))

real_list = mylist_thingy2('Z')
iterable = mygenerator_thingy2('Z')
iterable_list = list(iterable)

print(real_list)
print(iterable)
print(iterable_list)
#! lengths are supposed to be equal
print(set(iterable_list).intersection(real_list))
print(len(set(iterable_list).intersection(real_list))==len(real_list))
