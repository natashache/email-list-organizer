import csv
import sys

if not len(sys.argv) == 3:
	print("python3 email.py master.csv new.csv")
	exit()

masterEmailsFile = sys.argv[1]
newEmailsFile = sys.argv[2]

masterEmails = list([])
newEmails = list([])

newUniqueEmails = list([])

# Reading Csv files
with open(masterEmailsFile, newline='', encoding="utf8") as masterFile: # Added Encoding utf8 because, windows using ASCII as default
	reader =  csv.reader(masterFile)
	masterEmails = list(reader)

with open(newEmailsFile, newline='', encoding="utf8") as newFile:
	reader =  csv.reader(newFile)
	newEmails = list(reader)

# Finding Indexes for Email Address Columns in Both files
masterLabels = masterEmails[:1][0]
masterEmailColumn = masterLabels.index("Email Address")

newLabels = newEmails[:1][0]
newEmailColumn = newLabels.index("Email Address")

# Removing Labels from List
masterEmails = masterEmails[1:]
newEmails = newEmails[1:]

print("Master Emails: "+ str(len(masterEmails)))
print("New Emails: "+ str(len(newEmails)))

# Searching for Duplicate Records
for newLineItem in newEmails:
	
	found = False
	
	for oldLineItem in masterEmails:
		if(oldLineItem[masterEmailColumn].lower() == newLineItem[newEmailColumn].lower()):
			found = True
			break

	if not found:
		newUniqueEmails.append(newLineItem)

print("Unique Emails: "+ str(len(newUniqueEmails)))

# Prepanding Labels
newUniqueEmails = list([newLabels]) + newUniqueEmails

# Writing Unique Entries to new File
with open(newEmailsFile, 'w', newline='') as uniqueFile:
	wr = csv.writer(uniqueFile, quoting=csv.QUOTE_ALL)
	for row in newUniqueEmails:
		wr.writerow(row)