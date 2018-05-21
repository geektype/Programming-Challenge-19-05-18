#import the random module
from random import choice
#import the module we need to exit cleanly
from sys import exit

#the test bank with questions as their key and 
testBank = {}

#this block of code will open the file and process it
filename = 'testBank.txt'
with open(filename) as fh:
	#do this for every line in the file
    for line in fh:
    	#if a comma is present in the line meaning that there is a question answer pair
    	if ',' in line:
    		#set the question variable to the 1st string before the split and the second split string will be the answer
	        question, answer = line.strip().split(',', 1)
	        #finally add the id value pair to the testbank dictionary
	        testBank[question] = answer.strip()
#now the file is loaded in to a dictinary in the correct format


testQustions = {}
for i in range(10):
	qustion= str(choice(list(testBank.keys())))
	answer = testBank[qustion]
	print(answer)
	testQustions[qustion] = answer
print(testQustions)


# testing = True
# while testing:

