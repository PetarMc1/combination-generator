# Combination Generator
The Combination Generator is a Python script designed to generate all possible combinations of letters and numbers from a given input string. This tool allows you to specify the 
length of the combinations you wish to generate. The script organizes the generated combinations into text files within a designated folder, with each file named after the 
original input string.


## How it works
This Python script works by prompting you to input a string containing letters and numbers, as well as the desired length of combinations. It then utilizes the `itertools` module 
to generate all possible combinations of the specified length from the input string, allowing for repetition of characters. After generating the combinations, the script saves 
the unique combinations to a text file. Each file is named after the input string and stored in a `combinations` folder within the working directory. 
