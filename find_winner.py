#Find the winner
    
#Exercise: Import json file from server jsonplaceholder
# and print user/s with the largest number of correct attempts
# download json from https://jsonplaceholder.typicode.com/todos

from functions import *

tasksBase = 'https://jsonplaceholder.typicode.com/todos'
usersBase = 'https://jsonplaceholder.typicode.com/users'


myList = load_json(tasksBase)
true_answers = true_answer_counter(myList)
winers = find_winer(true_answers)

#sposob 1, pobieranie calej bazy i wyciaganie userow ktorzy wygrali
'''
r = requests.get(usersBase)
users = r.json()

print('The winer is:')
for user in users:
    for winer in winers:
        if winer == user['id']:
            print(user['name'])
'''

#sposob drugi, pobranie userow z wyfiltrowanej bazy wygranych (dopisek "?id=1&id=3)

prefix = '?'
i = 0
for user in winers:
    prefix = prefix+"id="+str(user)
    i +=1
    if i == len(winers):
        continue
    else:
        prefix += '&'

r = requests.get(usersBase+prefix)
users = r.json()
print('The winner is:')
for user in users:
    print(user['name'])
