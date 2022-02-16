import string 
import re

s = ''
with open('randomText.txt','r') as f:
    data = f.read()

#remove all characters except from letters and space    
data = re.sub(r'[^a-zA-Z]', ' ', data)

#create a list with words
list_of_words = data.split(' ')
for i in range(list_of_words.count('')):
    list_of_words.remove('')

#find the word with the most letters
max_length = 0

for word in list_of_words:
    if len(word) > max_length:
        max_length = len(word)
 

#create lists based on the length of the words
board_x = []
for x in range(max_length):
    board_y =[]   
    board_x.append(board_y)

for i in range(1,max_length+1):
    for word in list_of_words:
        if len(word) == i:
            board_x[i-1].append(word)

#remove 2 words each time with a sum of 20
if max_length >= 10:
    while len(board_x[9]) != 1:
        board_x[9].pop()
    for i in range(1,max_length-9):
        while(board_x[9-i] != [] and board_x[9+i] != []):
            board_x[9-i].pop()
            board_x[9+i].pop()

for i in range(1,max_length+1):
    print('words with ' +str(i) + " letters are: " +str(len(board_x[i-1])))
