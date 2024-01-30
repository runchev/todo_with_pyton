
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
    print("Netocni odgovori: ", str(netocen_odgovor), "/", len(data))
    print("Tocni odgovori: ", str(tocen_odgovor), "/", len(data))
