import os
import re
import openFiles

def extract_dataset(fileName):
    dataset = []
    directory_path = os.getcwd()
    infile = open(directory_path+fileName, 'r')
    for line in infile:
        line = line.strip()
        line = line.split()
        dataset.append(line)
    #print(dataset)
    infile.close()
    return dataset

def init_word_list():
    dataset = []
    directory_path = os.getcwd()
    infile = open(directory_path+"/onomatope.txt", 'r')
    for line in infile:
        line = line.strip()
        line = line.split(' ')
        dataset.append(line)
    infile.close()
    return dataset

def word_freq(word_list, data, mode):
    if (mode == 0):
        word_freq = []
        for line in range(len(data)):
            for word in range(len(word_list)):
                #print("WORD:", data[line][1], "== MIMETIC: ", mimetics[word][0])
                if (data[line][1] == word_list[word][0]):
                    word_freq.append(data[line])
        return word_freq
    elif (mode == 1):
        for file in range(len(data)):
            for line in range(len(data[file])):
                for word in range(len(word_list)):
                    if (data[file][word][1] == word_list[word][0]):
                        word_freq.append(data[line])
                    #for item in range(len(word_freq)):
                return word_freq
                

def write_out(freq_list, fileName):
    directory_path = os.getcwd()
    infile = open(directory_path+fileName+"_OUTPUT", 'w')
    writeFreq_list = []
    for line in range(len(freq_list)):
        currentLine = ""
        for section in range(len(freq_list[line])):
            #print(freq_list[line][section])
            if (section == 0):
                currentLine+=freq_list[line][section]
            else:
                currentLine+="\t"+freq_list[line][section]
        writeFreq_list.append(currentLine+'\n')
    for line in range(len(writeFreq_list)):
        #print(writeFreq_list[line])
        infile.write(writeFreq_list[line])
    infile.close()

def main():
    mode = 0
    inputFlag = False
    while (inputFlag == False):
        print("Please select read-out method:\n\t 1: Combine All\n\t 2: Individual Reports")
        input_data = input()
        mode = int(input_data)
        if (mode == 1 or mode == 2):
            inputFlag = True
        else:
            print("Please input valid data!")

    word_list = init_word_list()

    if (mode == 2):
        print("Please input file location: ")
        fileLocation = input()
        data = extract_dataset(fileLocation)
        freq_list = word_freq(word_list, data, 0)
        write_out(freq_list, fileLocation)

    elif (mode == 1):
        extract_all_data()
        data = extract_dataset(fileLocation)
        freq_list = word_freq(word_list, data, 1)
        write_out(freq_list, fileLocation)

main()
