#Zadanie 7.36


people = {
        "IcFDG2bO9AYDF651DoyH": {'name': 'John', 'age': 27, 'sex': 'Male'},
        "KcD9ntE6IRM59vkVta1k": {'name': 'Marie', 'age': 22, 'sex': 'Female'},
        "yDlgcn99xPc19mYXcRmy": {'name': 'Agness', 'age': 25, 'sex': 'Female'},
        "cpQh6GiAbBdGv35NDoTk": {'name': 'Nabeel', 'age': 17, 'sex': 'Male'},
        "12BifzWxCQySKgLhgahC": {'name': 'Jasmin ', 'age': 42, 'sex': 'Female'},
        "QLnmg0pzlLj9x7c7DlLv": {'name': 'Ruby', 'age': 55, 'sex': 'Female'},
        "To47urX0DUznWmOxGZ6H": {'name': 'Lori', 'age': 27, 'sex': 'Male'},
        "KQ4bir3y4tlkbG69I7zq": {'name': 'Marie', 'age': 42, 'sex': 'Female'},
        "94cp4hsyZP2BnCh4D34z": {'name': 'Agness', 'age': 25, 'sex': 'Female'},
        "Vr4wRdkljeEs46Czxo54": {'name': 'Chiara', 'age': 17, 'sex': 'Male'},          
         }
"""
[('IcFDG2bO9AYDF651DoyH', {'name': 'John', 'age': 27, 'sex': 'Male'}),
 ('KcD9ntE6IRM59vkVta1k', {'name': 'Marie', 'age': 22, 'sex': 'Female'}),
 ('yDlgcn99xPc19mYXcRmy', {'name': 'Agness', 'age': 25, 'sex': 'Female'}),
 ('cpQh6GiAbBdGv35NDoTk', {'name': 'Nabeel', 'age': 17, 'sex': 'Male'}),
 ('12BifzWxCQySKgLhgahC', {'name': 'Jasmin ', 'age': 42, 'sex': 'Female'}),
 ('QLnmg0pzlLj9x7c7DlLv', {'name': 'Ruby', 'age': 55, 'sex': 'Female'}),
 ('To47urX0DUznWmOxGZ6H', {'name': 'Lori', 'age': 27, 'sex': 'Male'}),
 ('KQ4bir3y4tlkbG69I7zq', {'name': 'Marie', 'age': 42, 'sex': 'Female'}),
 ('94cp4hsyZP2BnCh4D34z', {'name': 'Agness', 'age': 25, 'sex': 'Female'}),
 ('Vr4wRdkljeEs46Czxo54', {'name': 'Chiara', 'age': 17, 'sex': 'Male'})]
"""
ppllist2 = [
            ('John', 27, 'Male'),
            ('John3', 22, 'Male'),
            ('John2', 11, 'Male')   
           ]


people2 = [
         {'id': 'IcFDG2bO9AYDF651DoyH', 'name': 'John', 'age': 27, 'sex': 'Male'},
         {'id': 'KcD9ntE6IRM59vkVta1k', 'name': 'Marie', 'age': 22, 'sex': 'Female'},
         {'id': 'yDlgcn99xPc19mYXcRmy', 'name': 'Agness', 'age': 25, 'sex': 'Female'}               
        ]

people3 = ["Arkadiusz",
           "Wiola",
           "Kuba"
          ]

'''
for key in people2:
    for id in key:
        print(id, ":", key[id])


for data in people:
    print(people[data])
'''
'''
for data in people2:
    for name in data:
        if name == 'name':
            print(data[name])

for dict in people:
    for name in people[dict]:
        if name == 'name':
            print(people[dict][name])
'''

for id, data in people.items():
    for name in data:
        if name == 'name':
            print(id, ':', data[name])
        
