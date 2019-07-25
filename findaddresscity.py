import requests
import re

number = int(input("Please enter the street number: "))
street = input("Please enter the street name: ")
street = street.replace(' ', '+')
strnumber = str(number)

link = "https://www.google.com/maps/place/" + strnumber + "+" + street

f = requests.get(link)
massivetext = f.text

pattern = re.compile(r', [A-Z]{2} [0-9]{5}')
numberindex = []
matches = pattern.finditer(massivetext)
for match in matches:
    numberindex.append(match)

lastwebstring1 = str(numberindex[0])
startpos = (lastwebstring1.find(',')) + 2
endpos = (lastwebstring1.find(')'))
finalnum = int(lastwebstring1[startpos:endpos])
firstnum = finalnum - 50
finalstring = massivetext[firstnum:finalnum]

yes = finalstring.find("\"")
print(finalstring[yes+5:])

