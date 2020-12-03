import os
import win32api


def get_drives():
    drives = win32api.GetLogicalDriveStrings()
    drives = drives.split('\000')[:-1]
    return drives


def get_files(counter, directory="C:\\", ext=".pdf"):
    for root, sub, file in os.walk(directory):

        # print(root)
        # print(sub)
        pdf = [f for f in file if f.endswith(ext)]
        if pdf:
            # print(pdf)

            for file1 in pdf:
                counter = counter+1
                print(str(counter) + ":" + root + "\\" + file1)


drives = get_drives()
counter = 0
for drive in drives:

    print(drive)
    get_files(counter, drive, ".pdf")




