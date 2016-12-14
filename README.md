# deletr
attempt at a file scanner and date based removal

deleter.py is the file removal process currently at rough draft stage/rev 1

aservice.py is stolen from http://ryrobes.com/category/python/ and in theory (untested) will allow the python script to run as a windows service

delete lines are commented out for safety during testing, replaced with print commands

current issues to be addressed:

permissions - this may be addresed by running as a service, yet to test

clean up and commenting

universalisation (is that a word?) - add prompt for top most directory to be scanned, this was designed to run only on one pc in one location

