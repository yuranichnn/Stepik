jsomList = [
    {"name": "A", "parents": []},
    {"name": "B", "parents": ["A", "C"]},
    {"name": "C", "parents": ["A"]}
    ]

jsomList = [
{'name': 'E', 'parents': []},
{'name': 'A', 'parents': ['E']},
{'name': 'B', 'parents': []},
{'name': 'C', 'parents': ['A', 'B']},
{'name': 'D', 'parents': ['C', 'B']},
]

listRex = {}
for item in jsomList:
    keyTmp = item['name']
    paramTmp = item['parents']
    if keyTmp not in listRex:
        listRex.update({keyTmp:1})
    for item2 in jsomList:
        if keyTmp in item2['parents']:
            listRex[keyTmp] = listRex[keyTmp] + 1

for key, val in listRex.items():
    print(key + ' : ' + str(val))
