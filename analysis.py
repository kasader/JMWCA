import os
import re

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

def create_mimetic_list():
    dataset = []
    directory_path = os.getcwd()
    infile = open(directory_path+"/onomatope.txt", 'r')
    for line in infile:
        line = line.strip()
        line = line.split(' ')
        dataset.append(line)
    infile.close()
    return dataset

def mimetic_freq(mimetics, data):
    mimetic_freq = []
    for line in range(len(data)):
        for word in range(len(mimetics)):
            #print("WORD:", data[line][1], "== MIMETIC: ", mimetics[word][0])
            if (data[line][1] == mimetics[word][0]):
                mimetic_freq.append(data[line])
    return mimetic_freq

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
    mimetics = create_mimetic_list()
    #print(mimetics_list)
    #for word in range(len(mimetics_list)):
    #    print("Mimetic [%d]: %s" % (word, mimetics_list[word]))
    print("Please input file location: ")
    fileLocation = input()
    data = extract_dataset(fileLocation)
    freq_list = mimetic_freq(mimetics, data)
    write_out(freq_list, fileLocation)
    #print(freq_list, fileLocation)
    #dataset = list(filter(None, dataset))
    #print("Dataset: "+str(dataset))
    # for i in range(len(dataset)):
        # print("Dataset: "+str(dataset[i]))
        #for j in range(len(dataset[i])):
            #print(dataset[i][j])


main()
