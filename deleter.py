import os
import sys
import datetime

def main():
    save_out = sys.stdout
    f = "deletion_log.log"
    fsock = open(f, 'a')
    sys.stdout = fsock
    for root, dirs, files in os.walk('D:', topdown=False):
        for name in files:
            duration = timeCalc(root, name)
            if duration.days > 100:
                try:
                    print("deleted: ", os.path.join(root, name), datetime.datetime.today())
                    #os.remove(os.path.join(root, name))
                except OSError:
                    print("failed to delete: ", os.path.join(root, name), datetime.datetime.today())
                    continue
            else:
                continue
        for name in dirs:
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
    sys.stdout = save_out
    fsock.close()


def timeCalc(root, att):
    try:
        return datetime.datetime.today() - datetime.datetime.fromtimestamp(os.path.getmtime(os.path.join(root, att)))
    except PermissionError:
        print("DENIED ACCESS: ", os.path.join(root, att), datetime.datetime.today())
        return datetime.timedelta(days=0)


main()
