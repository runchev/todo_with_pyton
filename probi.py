# import random
# lower_bound = int(input("Insert lower bound: "))
# higher_bound = int(input("Insert higher bound: "))
#
# try:
#     print(random.randint(lower_bound, higher_bound))
# except ValueError:
#     print("Invalid input, try again!")

import json

with open("questions.json", "r") as file:
    content = file.read()
tocen_odgovor = 0
netocen_odgovor = 0
data = json.loads(content)
for question in data:
    print(question['question_text'])
    for index, ponudeni_odgovori in enumerate(question['ponudeni_odgovori']):
        print(int(index)+1, "-", ponudeni_odgovori)
    odgovor = input("Vnesi go odgovorot: ")
    if int(odgovor) == question['tocen_odgovor']:
        tocen_odgovor = tocen_odgovor+1
    else:
        netocen_odgovor = netocen_odgovor+1
    print("Tocni odgovori: ", str(tocen_odgovor), "/", len(data))
    print("Netocni odgovori: ", str(netocen_odgovor), "/", len(data))