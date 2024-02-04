import os

folders = input("provide a list of folders with spaces: ").split()
print(folders)

for folder in folders:
    files = os.listdir(folder)
    print(files)