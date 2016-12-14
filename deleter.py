import os
import datetime

def main():
    for root, dirs, files in os.walk('D:', topdown=False):
        for name in files:
            duration = timeCalc(root, name)
            if duration.days > 100:
                try:
                    print("delete")#os.remove(os.path.join(root, name))
                except OSError:
                    print("fail")
                    print(os.path.join(root, name))
            else:
                print(os.path.join(root, name))
                print("keep")
        for name in dirs:
            duration = timeCalc(root, name)
            if duration.days > 100:
                try:
                    print("delete")#os.remove(os.rmdir.join(root, name))
                except OSError:
                    print("fail")
                    print(os.path.join(root, name))
                    continue
            else:
                print(os.path.join(root, name))
                print("Keep")

def timeCalc(root, att):
    try:
        fileOrFolder = os.path.join(root, att)
        times = datetime.datetime.fromtimestamp(os.path.getmtime(fileOrFolder))
        duration = datetime.datetime.today() - times
        print(os.path.join(root, att))
        print(times)
        print(duration)
        return duration
    except PermissionError:
        print("DENIED")
        duration = datetime.timedelta(days=0)
        return duration

if __name__ == "__main__"
    main()
