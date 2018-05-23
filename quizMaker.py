#import the random module
from random import choice
#import the module we need to exit cleanly
from sys import exit

#the test bank with questions as their key and answer as the value
testBank = {}
#Points to keep track of the corrct answers
points = 0

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


#this block will use the existing the test bank to make another dictinary of 10 question
#that will be tester
#the dictionary for the 10 questions
testQustions = {}
#the for loop that will run 10 times
for i in range(10):
	#chose a random qustions from the test bank
	qustion= str(choice(list(testBank.keys())))
	#the answer will the the value of the quation
	answer = testBank[qustion]
	#add the question answer pair to the dictionary
	testQustions[qustion] = answer


#Test Loop
testing = True
while testing:
	for question in testQustions:
		print(question + '\n')
		userAns = str(input(">>>"))
		if userAns == testQustions[question]:
			print("correct!")
			points += 1
		else:
			print("sorry what you entered is wrong!", "the answer is : ", str(testQustions[question]))
	testing = False

print("quiz finished. Out of 10 points you scored", str(points), "point(s)")

print("Do you want to save your score?")
resp = str(input(">>>"))

if resp == "yes" or resp == "y":
	name = str(input("Enter your name"))
else:
	exit()

hsFile = "highscore.txt"
with open(hsFile, 'a') as hs:
	line = 	name + "," + str(points) + "\n"
	hs.write(line)
