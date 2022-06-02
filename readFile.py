# readFile.py
import os
import re

def extract_dataset(dataset):
    mode = 0
    inputFlag = False
    while (inputFlag == False):
        print("Please choose file selection method:\n\t1) File in ./input_data/"
              "\n\t2) File in ./\n\t3) Other")
        input_data = input()
        mode = int(input_data)
        if (0 < mode < 4):
            inputFlag = True
        else:
            print("Please input valid selection!")

    directory_path = os.getcwd()

    if (mode == 1):
        print("Please enter file name:")
        filename = input()
        directory_path += filename
        dataset.name = filename
        dataset.location = directory_path
    elif (mode == 2):
        print("Please enter file name:")
        filename = input()
        directory_path += "/input_data/" + filename
        dataset.name = filename
        dataset.location = directory_path
    else:
        print("Please enter file location:")
        directory_path = input()
        dataset.location = directory_path
        temp = re.split("/", dataset.location)
        dataset.name = temp[len(temp)-1]

    if os.path.isfile(dataset.location):
        infile = open(dataset.location)
        for line in infile:
            line = line.strip()
            line = line.split()
            dataset.text.append(line)
        infile.close()
        return dataset
    else:
        print("File path is invalid!")
        exit(0)
    #print("Name is:", dataset.name)


"""
    files = os.listdir(directory_path)
    allData = []
    for files in files:
        dataset = []
        if os.path.isFile(os.path.join(directory_path, file)):
            infile = open (os.path.join(directory_path, file), 'r')
            for line in infile:
                line = line.strip()
                line = line.split()
                dataset.append(line)
            allData.append(dataset)
            infile.close()
        return allData
"""
