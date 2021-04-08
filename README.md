# Email List Organizer

Steps to run the script are as follows:
1.	Install python3.x on your pc/mac
2.	Clone/Download Git repository
3.	Copy master email and new email list files (.i.e. master.csv and new.csv)
4.	Run command `python3 email.py master.csv new.csv`
 
1-3 Steps needed to be done only once if you don’t have python and GitHub repo setup on your pc/mac.
Duplicate email will be removed from New.csv after running the command
 
Email Column name need to be “Email Address” as it was given in example Google Sheets

To create csv with unique emails run following command in console:
```
python3 email.py master.csv new.csv
```