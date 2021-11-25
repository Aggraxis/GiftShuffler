# GiftShuffler
Take a CSV of participants and generate text files for blind gift giving.

We have this thing where someone in the family sets up a secret gift exchange for Christmas. We enjoy it, but the organizer always knows all of the giving pairs, eliminating some of the surprise. This little toy reads a list of names from a CSV and matches up some random assignments for gift giving. It then writes out a series of text files to send to the participants. DON'T OPEN THE FILES if you don't want to know the details.

The script checks for self giving, but no other validation (spouses, siblings, etc.) is assumed. Everyone is fair game as a recipient except for the giver. That would just be silly.

Have fun!

-Aggraxis

Usage:
 - Install Python 3: https://www.python.org/
 - Clone this repository or just download GiftShuffler.py and participants.csv into the same folder
 - Edit participants.csv with your desired list of names. 
   - Most PCs will probably try to open the file with Excel, which is fine so long as you save the file as a Comma Separated Values (CSV) file instead of an Excel spreadsheet. Editing it in something like Notepad or Notepad++ works too. Keep in mind that the column header still needs to say NAME because the code looks for it.
 - Open up a terminal, command prompt, Powershell window, or whatever and navigate to where you stored the files. 
   - Putting them somewhere simple like c:\shuffler\ might help.
 - execute the script: python GiftShuffler.py
   - It won't return any output to the terminal, but you should see a series of 'send_to_(person).txt' files in your shuffler folder now.
 - Don't open the text files! Send them to the person indicated in the file name.
   - For example, the file for me might be named 'send_to_paul.txt', and the contents would read something like 'Paul gives to Ben'
 - Commence gifting mayhem.
 
