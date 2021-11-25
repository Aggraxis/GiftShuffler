#import os
import random
import csv

if __name__ == "__main__":
    fileName="participants.csv"
    participantList = []
    with open (fileName) as csvfile:
        reader = csv.DictReader(csvfile)
        participantList = list(reader)
    recipientList = participantList.copy()
    givingDict = {}
    for participant in participantList:
        #this is most likely not pythonic.
        found = False
        while not(found):
            potentialRecipient = random.choice(recipientList)
            if participant['NAME'] != potentialRecipient['NAME']:
                givingDict[participant['NAME']] = potentialRecipient['NAME']
                recipientList.remove(potentialRecipient)
                found = True
    for key in givingDict:
        outFileName="send_to_" + key + ".txt"
        text_file = open(outFileName, "wt")
        n = text_file.write(f'{key} gives to {givingDict[key]}\n')
        text_file.close()



