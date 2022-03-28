#1a
from curses.ascii import isdigit
import numbers


my_list = ['Jens','Hans','sine','max','Hanne','Helle','Mikkel']
test = 'H'
print(my_list)
res = [idx for idx in my_list if idx[0].lower() == test.lower()]
print("list elements with letter H:",res)

#1b

#1c

name = "peter"

this_tuple = (len(name),name)

print("lenght of name: ", this_tuple)

#1D
string_sentence = "6 days ago"

numbers = []
for element in string_sentence.split(): 
    if element.isdigit():
        numbers.append(int(element))

print("number in sentence: ",numbers)

second_dice = {'1','2','3','4','5','6'}
first_dice = {'1','2','3','4','5','6'}

combos = {f+' '+s for s in second_dice for f in first_dice}


print(combos)

