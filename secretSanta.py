###### Secret Santa Email generator ###########

#Input: text file copied over from outlook. Input should be delimited by ";" and emails should be nested within "<" ">" characters as standard

#Process of script:
#   (0) Create dictiornary with name and email address
#   (1) Randomly arrange list of names using random numbers associated with each user
#   (2) Assign secret santas based on randomly generated numbers
#   (3) Send out emails for secret santa assignments

# Output: "automates emails from your email address"
# Additional features: Store information of who has who in a hidden database for reference

import random
import csv


#Declare delimiters
delim1 = ";"
delim2 = "<"

#read text file and split at ";" delimiter
with open('Email list.txt') as f:
    t = f.readline()
    dicts = t.split(delim1)

db = []
index = []
randints = []

for count, sub in enumerate(dicts):
    if count ==0:
        name = name = sub.split(delim2)[0][0:-1]
    else:
        name = sub.split(delim2)[0][1:-1]
    email = sub.split(delim2)[1][:-1]
    index.append(count)
    randint = random.random()
    randints.append(randint)
    db.append([count, name, email, randint])

Z = [x for _,x in sorted(zip(randints,index))]

for count, x in enumerate(Z):
    user_key = x
    assigned = x-1
    db[count].append(db[assigned][1])  

for count, x in enumerate(db):
    print(x[1]+", You have been assigned " + x[4] + " to gift them a present")



