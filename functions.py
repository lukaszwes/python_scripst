#Functions for "Find the winner" exercise (main file is find_winner.py)

import requests
import json
#address = 'https://jsonplaceholder.typicode.com/todos'

def load_json (address):
    try:
        r = requests.get(address)
        jsonBase = r.json()
    except requests.ConnectionError:
        return print('Podales nieprawidlowy adres')
    except requests.exceptions.SSLError:
        return print('Podales adres do nieprawidlowej bazy json')
    except json.JSONDecodeError:
        return print('Podales adres do nieprawidlowej bazy json')
    else:
        return jsonBase

def true_answer_counter (jsonfile):
    userList = {}
    for line in jsonfile:
        if line['completed'] == True:
            try:
                userList[line['userId']] += 1
            except KeyError:
                userList[line['userId']] = 1
    return userList

def find_winer (users):
    users = users.items()
    maxTrueAnswers = max(users)[1]
    winer = [user
              for user, result in users
              if result == maxTrueAnswers]
    return winer

