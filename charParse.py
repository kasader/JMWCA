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
