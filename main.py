import itertools
import os

def generate_combinations(input_string, combination_length):
    input_string = ''.join(sorted(set(input_string), key=input_string.index))

    combinations = itertools.permutations(input_string, combination_length)

    return combinations

def save_combinations_to_file(combinations, input_string):
    directory = 'combinations'
    if not os.path.exists(directory):
        os.makedirs(directory)

    filename = os.path.join(directory, f'{input_string}.txt')
    with open(filename, 'w') as file:
        file.write(f"All combinations are generated from the characters and numbers: {input_string}\n\n")
        for combination in combinations:
            file.write(''.join(combination) + '\n')

    print(f'Combinations saved to {filename}')

if __name__ == "__main__":
    input_string = input("Enter the string of letters and numbers: ")
    combination_length = int(input("Enter the length of combinations: "))

    combinations = generate_combinations(input_string, combination_length)
    save_combinations_to_file(combinations, input_string)
