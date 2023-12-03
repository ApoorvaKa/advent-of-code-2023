# Advent of Code Day 2 Puzzle

import re

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

def extract_game_number(game_string):
    game_number = re.search(r"Game (\d+):", game_string).group(1)
    return game_number

def is_round_valid(round_string):
    num_red = re.search(r"(\d+) red", round_string).group(1) if re.search(r"(\d+) red", round_string) else 0
    num_green = re.search(r"(\d+) green", round_string).group(1) if re.search(r"(\d+) green", round_string) else 0
    num_blue = re.search(r"(\d+) blue", round_string).group(1) if re.search(r"(\d+) blue", round_string) else 0
    return int(num_red) <= MAX_RED and int(num_green) <= MAX_GREEN and int(num_blue) <= MAX_BLUE


def is_game_valid(game_string):
    round_list = game_string.split(";")
    for round in round_list:
        if not is_round_valid(round):
            return False
    return True

def get_sum_of_valid_games(file_name):
    try:
        file = open(file_name, "r")
    except FileNotFoundError:
        print("File not found!")
        return -1
    total = 0
    for line in file:
        line = line.strip()
        if is_game_valid(line):
            total += int(extract_game_number(line))
    return total

def get_game_power(game_string):
    round_list = game_string.split(";")
    min_red, min_green, min_blue = 0, 0, 0
    for round in round_list:
        num_red = re.search(r"(\d+) red", round).group(1) if re.search(r"(\d+) red", round) else 0
        min_red = max(min_red, int(num_red))
        num_green = re.search(r"(\d+) green", round).group(1) if re.search(r"(\d+) green", round) else 0
        min_green = max(min_green, int(num_green))
        num_blue = re.search(r"(\d+) blue", round).group(1) if re.search(r"(\d+) blue", round) else 0
        min_blue = max(min_blue, int(num_blue))
    return (min_red * min_green * min_blue)


def get_power_sum(file_name):
    try:
        file = open(file_name, "r")
    except FileNotFoundError:
        print("File not found!")
        return -1
    power_sum = 0
    for line in file:
        line = line.strip()
        power_sum += get_game_power(line)
    return power_sum


def main():
    print(get_sum_of_valid_games("input.txt"))
    print(get_power_sum("input.txt"))

if __name__ == "__main__":
    main()
