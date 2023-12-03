WORD_TO_NUMBER = {
    "one" : 1,
    "two" : 2,
    "three" : 3,
    "four" : 4,
    "five" : 5,
    "six" : 6,
    "seven" : 7,
    "eight" : 8,
    "nine" : 9,
}

def calibrate_line(line):
    first_number = None
    curr_word = ""
    for val in line:
        if val.isnumeric():
            if first_number is None:
                first_number = val
            last_number = val
            curr_word = ""
        else:
            curr_word += val
            print(curr_word)
            if curr_word in WORD_TO_NUMBER:
                print(curr_word)
                if first_number is None:
                    first_number = str(WORD_TO_NUMBER[curr_word])
                last_number = str(WORD_TO_NUMBER[curr_word])
                curr_word = ""

    print("{} : {}". format(line, first_number + last_number))
    return int(first_number + last_number )

def calibration(input_file):
    try:
        file = open(input_file, 'r')
    except FileNotFoundError:
        print("File not found")
        return

    total = 0
    for line in file:
        curr_calibration = calibrate_line(line.strip())
        total += curr_calibration
        
    return total


def main():
    print("The calibration is: {}".format(calibration("input.txt")))

if __name__ == "__main__":
    main()