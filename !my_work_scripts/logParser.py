from sys import argv

filename = argv

with open(filename[1]+'.txt', encoding='utf-16') as file_object:
    lines = file_object.readlines()

for line in lines:
    if "To be installed;" in line:
        filePath = line.split(';', 1)[0].split('File: ', 1)[1]
        print(filePath)
        outputFilename = 'installedFiles_'+filename[1]+'.tre'
        with open(outputFilename, 'a') as f:
            f.write("\n"+filePath)