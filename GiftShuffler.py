import random
import csv

if __name__ == "__main__":
    fileName="participants.csv"
    giverList = []
    givingDict = {}
    exclusionDict = {}
    
    with open (fileName) as csvfile:
        reader = csv.DictReader(csvfile)
        giverDicts = list(reader)
    with open (fileName) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            exclusionDict[row['NAME']] = row['PARTNER']
            exclusionDict[row['PARTNER']] = row['NAME']

    giverList = [gDict['NAME'] for gDict in giverDicts]
    recipientList = giverList.copy()

    for giver in giverList:
        found = False
        while not(found):
            recipient = random.choice(recipientList)
            if giver != recipient and recipient != exclusionDict[giver]:
                givingDict[giver] = recipient
                recipientList.remove(recipient)
                found = True
            
    for key in givingDict:
        outFileName="send_to_" + key + ".txt"
        text_file = open(outFileName, "wt")
        n = text_file.write(f'{key} gives to {givingDict[key]}\n')
        text_file.close()



