import os

for folderName, subFolders, fileNames in os.walk('C:\\Users\\Shaquille Mandy\\Desktop\\'):
    print("The folder is " + folderName)
    print()
    print("These are the subfolders in " + folderName)
    for eachsubfolder in subFolders:
        print("\t" + eachsubfolder)
    print()
    print("These are the files")
    for eachfile in fileNames:
        print('\t' + eachfile)
    print()
    print('-' * 120)
