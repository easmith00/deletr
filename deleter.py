import os
import sys
import datetime

def main():
    save_out = sys.stdout                                                                                               # save the current stream (all print commands)                                                                                           # defines the log file
    fsock = open("deletion_log.log", "a")                                                                               # open the log file for appending
    sys.stdout = fsock
    for root, dirs, files in os.walk('D:', topdown=False):                                                              # generate tuple for directory and files
        for name in files:                                                                                              # start loop to look for files that are too old
            duration = timeCalc(root, name)                                                                             # call process to create a file age
            if duration.days > 100:                                                                                     # check if file is aged out
                try:
                    print("deleted: ", os.path.join(root, name), datetime.datetime.today())                             # send deleted file details to log
                    #os.remove(os.path.join(root, name))                                                                # delete file
                except OSError:                                                                                         # just in case fails
                    print("failed to delete: ", os.path.join(root, name), datetime.datetime.today())                    # send failure details to log
                    continue
            else:
                continue
        for name in dirs:                                                                                               # same as above for directories
            duration = timeCalc(root, name)
            if duration.days > 100:
                try:
                    print("deleted: ", os.path.join(root, name), datetime.datetime.today())
                    #os.remove(os.rmdir.join(root, name))
                except OSError:
                    print("failed to delete: ", os.path.join(root, name), datetime.datetime.today())
                    continue
            else:
                continue
    sys.stdout = save_out                                                                                               # stop logging
    fsock.close()                                                                                                       # close file


def timeCalc(root, att):
    try:
        return datetime.datetime.today() - datetime.datetime.fromtimestamp(os.path.getmtime(os.path.join(root, att)))   # work out age of file in days
    except PermissionError:
        print("DENIED ACCESS: ", os.path.join(root, att), datetime.datetime.today())                                    # because something keeps failing on one file in test group
        return datetime.timedelta(days=0)                                                                               # set to 0 to prevent attempted deletion of irritating file


main()
