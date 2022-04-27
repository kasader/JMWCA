import os

def extract_dataset(word_list):
    directory_path = os.getcwd()
    directory_path += "/input_data"
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

            

